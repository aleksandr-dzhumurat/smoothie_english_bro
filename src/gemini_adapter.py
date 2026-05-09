import mimetypes
import os
import struct

from dotenv import load_dotenv
from google import genai
from google.genai import types

print(f'Load environment variables from .env file: {load_dotenv()}')

def save_binary_file(file_name, data):
    with open(file_name, "wb") as f:
        f.write(data)
    print(f"File saved to: {file_name}")

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
        elif param.startswith("audio/L"):
            try:
                bits_per_sample = int(param.split("L", 1)[1])
            except (ValueError, IndexError):
                pass
    return {"bits_per_sample": bits_per_sample, "rate": rate}

def generate_text(system_prompt, user_prompt, model="gemini-2.0-flash"):
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

def generate_speech(text_input, output_base_name):
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    model = "gemini-2.5-flash-preview-tts" # Updated to a stable version that supports TTS
    contents = [
        types.Content(
            role="user",
            parts=[types.Part.from_text(text=text_input)],
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

    audio_chunks = []
    usage_metadata = None
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        if chunk.usage_metadata:
            usage_metadata = chunk.usage_metadata
        if chunk.parts is None:
            continue
        if chunk.parts[0].inline_data and chunk.parts[0].inline_data.data:
            inline_data = chunk.parts[0].inline_data
            data_buffer = inline_data.data
            file_extension = mimetypes.guess_extension(inline_data.mime_type)
            if file_extension is None:
                file_extension = ".wav"
                data_buffer = convert_to_wav(inline_data.data, inline_data.mime_type)
            audio_chunks.append((data_buffer, file_extension))
        elif chunk.text:
            print(f"Assistant: {chunk.text}")

    if usage_metadata:
        print(f"Tokens: input={usage_metadata.prompt_token_count}, output={usage_metadata.candidates_token_count}")

    for file_index, (data_buffer, file_extension) in enumerate(audio_chunks):
        file_name = f"{output_base_name}_{file_index}{file_extension}"
        save_binary_file(file_name, data_buffer)

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
