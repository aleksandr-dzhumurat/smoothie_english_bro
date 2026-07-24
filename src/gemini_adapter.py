import logging
import os
import struct
import subprocess
import time
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai import errors, types

import azure_tts

print(f'Load environment variables from .env file: {load_dotenv()}')

DEFAULT_MODEL = os.environ.get('GEMINI_MODEL', 'gemini-2.0-flash')
DEFAULT_TTS_MODEL = os.environ.get('GEMINI_TTS_MODEL', 'gemini-2.5-flash-preview-tts')
GEMINI_TTS_PROMPT = (
    'Read the transcript aloud verbatim in a slow, steady voice for an English learner. '
    'Aim for about 70 percent of your normal speaking pace, with clear articulation '
    'and brief, natural pauses. Read only the transcript, not these instructions or the label.\n\n'
    'Transcript:\n'
)
logger = logging.getLogger(__name__)

def convert_to_wav(audio_data: bytes, mime_type: str) -> bytes:
    parameters = parse_audio_mime_type(mime_type)
    bits_per_sample = parameters["bits_per_sample"]
    sample_rate = parameters["rate"]
    num_channels = 1
    data_size = len(audio_data)
    bytes_per_sample = bits_per_sample // 8
    block_align = num_channels * bytes_per_sample
    byte_rate = sample_rate * block_align
    chunk_size = 36 + data_size

    header = struct.pack(
        "<4sI4s4sIHHIIHH4sI",
        b"RIFF",
        chunk_size,
        b"WAVE",
        b"fmt ",
        16,
        1,
        num_channels,
        sample_rate,
        byte_rate,
        block_align,
        bits_per_sample,
        b"data",
        data_size
    )
    return header + audio_data

def parse_audio_mime_type(mime_type: str) -> dict[str, int | None]:
    bits_per_sample = 16
    rate = 24000
    parts = mime_type.split(";")
    for param in parts:
        param = param.strip()
        if param.lower().startswith("rate="):
            try:
                rate_str = param.split("=", 1)[1]
                rate = int(rate_str)
            except (ValueError, IndexError):
                pass
        elif param.lower().startswith("audio/l"):
            try:
                bits_per_sample = int(param[len("audio/L"):])
            except (ValueError, IndexError):
                pass
    return {"bits_per_sample": bits_per_sample, "rate": rate}


def _encode_mp3(audio_data: bytes) -> bytes | None:
    try:
        result = subprocess.run(
            ["ffmpeg", "-hide_banner", "-loglevel", "error", "-i", "pipe:0", "-f", "mp3", "pipe:1"],
            input=audio_data, capture_output=True, check=True, timeout=60,
        )
        return result.stdout
    except FileNotFoundError:
        logger.warning('tts_encoding_failed reason=ffmpeg_not_found using_original_audio=true')
        return None
    except subprocess.CalledProcessError as error:
        logger.warning('tts_encoding_failed reason=ffmpeg_exit exit_code=%s using_original_audio=true', error.returncode)
        return None


def generate_text(system_prompt, user_prompt, model=None):
    model = model or DEFAULT_MODEL
    client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
    response = client.models.generate_content(
        model=model,
        contents=user_prompt,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=0.1,
            max_output_tokens=3000,
        ),
    )
    return response.text

def is_quota_error(error: errors.APIError) -> bool:
    return error.code == 429 or error.status == 'RESOURCE_EXHAUSTED'


def generate_speech(text_input, output_base_name):
    """Use Gemini for speech, falling back to Azure on quota or other speech errors."""
    started = time.monotonic()
    logger.info('tts_provider_started provider=gemini model=%s chars=%s', DEFAULT_TTS_MODEL, len(text_input))
    try:
        return _generate_gemini_speech(text_input, output_base_name)
    except Exception as error:
        logger.warning('tts_provider_failed provider=gemini error_type=%s api_code=%s elapsed_s=%.2f fallback=azure',
                       type(error).__name__, error.code if isinstance(error, errors.APIError) else None,
                       time.monotonic() - started)
        return azure_tts.generate_speech(text_input, output_base_name)


def _generate_gemini_speech(text_input, output_base_name):
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    model = DEFAULT_TTS_MODEL
    contents = [
        types.Content(
            role="user",
            parts=[types.Part.from_text(text=GEMINI_TTS_PROMPT + text_input)],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        temperature=1,
        response_modalities=["audio"],
        speech_config=types.SpeechConfig(
            voice_config=types.VoiceConfig(
                prebuilt_voice_config=types.PrebuiltVoiceConfig(voice_name="Zephyr")
            )
        ),
    )

    audio_data = bytearray()
    mime_type = None
    usage_metadata = None
    chunks = 0
    finish_reasons = set()
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        chunks += 1
        for candidate in chunk.candidates or ():
            if isinstance(candidate.finish_reason, types.FinishReason):
                finish_reasons.add(candidate.finish_reason.value)
        if chunk.usage_metadata:
            usage_metadata = chunk.usage_metadata
        if not chunk.parts:
            continue
        if chunk.parts[0].inline_data and chunk.parts[0].inline_data.data:
            inline_data = chunk.parts[0].inline_data
            mime_type = inline_data.mime_type or mime_type
            audio_data.extend(inline_data.data)

    if usage_metadata:
        logger.info('tts_usage provider=gemini input_tokens=%s output_tokens=%s',
                    usage_metadata.prompt_token_count, usage_metadata.candidates_token_count)

    if not audio_data:
        logger.warning('tts_no_audio provider=gemini chunks=%s finish_reasons=%s',
                       chunks, ','.join(sorted(finish_reasons)) or 'none')
        return None

    mime_type = mime_type or 'audio/L16;rate=24000'
    data_buffer = bytes(audio_data)
    logger.info('tts_stream_completed provider=gemini chunks=%s audio_bytes=%s', chunks, len(data_buffer))
    if mime_type.lower().startswith(('audio/l', 'audio/pcm')):
        data_buffer = convert_to_wav(data_buffer, mime_type)

    mp3_audio = _encode_mp3(data_buffer)
    if mp3_audio is not None:
        file_name = f"{output_base_name}_0.mp3"
        Path(file_name).write_bytes(mp3_audio)
    else:
        file_name = f"{output_base_name}_0.wav"
        Path(file_name).write_bytes(data_buffer)
    return file_name

if __name__ == "__main__":
    print("--- Smoothie English Dialogue Loop ---")
    print("Enter text to generate speech (type 'exit' to quit).")
    
    dialogue_counter = 0
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        
        if not user_input.strip():
            continue
            
        output_name = f"speech_output_{dialogue_counter}"
        generate_speech(user_input, output_name)
        dialogue_counter += 1
