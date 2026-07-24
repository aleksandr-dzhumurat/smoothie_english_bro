import logging
import os
import re
from pathlib import Path
from xml.sax.saxutils import escape

import httpx


# Only English voices are supported. Azure voice names include the locale.
VOICES = {
    'en-GB-SoniaNeural',
    'en-GB-RyanNeural',
    'en-US-JennyNeural',
    'en-US-GuyNeural',
}
DEFAULT_VOICE = 'en-GB-SoniaNeural'
DEFAULT_SPEED = 0.7
logger = logging.getLogger(__name__)


def generate_speech(
    text_input: str,
    output_base_name: str,
    *,
    voice: str = DEFAULT_VOICE,
    speed: float = DEFAULT_SPEED,
) -> str | None:
    """Synthesize English speech with Azure and return the MP3 path."""
    if voice not in VOICES:
        raise ValueError(f'Unsupported Azure English voice: {voice}')
    if not 0.5 <= speed <= 2.0:
        raise ValueError('Azure speech speed must be between 0.5 and 2.0')
    if not text_input.strip():
        return None

    key = os.environ.get('AZURE_SPEECH_KEY', '').strip()
    region = os.environ.get('AZURE_SPEECH_REGION', '').strip()
    if not key or not region:
        logger.warning('tts_not_configured provider=azure missing_key=%s missing_region=%s', not key, not region)
        raise RuntimeError('Set AZURE_SPEECH_KEY and AZURE_SPEECH_REGION to enable Azure TTS')
    if not re.fullmatch(r'[a-z0-9-]+', region):
        raise ValueError('AZURE_SPEECH_REGION must be an Azure region identifier')

    locale = voice.rsplit('-', 1)[0]
    rate = f'{(speed - 1) * 100:+g}%'
    ssml = (
        f'<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="{locale}">'
        f'<voice name="{voice}"><prosody rate="{rate}">{escape(text_input)}</prosody></voice>'
        '</speak>'
    )
    logger.info('tts_provider_started provider=azure voice=%s chars=%s', voice, len(text_input))
    response = httpx.post(
        f'https://{region}.tts.speech.microsoft.com/cognitiveservices/v1',
        content=ssml.encode('utf-8'),
        headers={
            'Ocp-Apim-Subscription-Key': key,
            'Content-Type': 'application/ssml+xml',
            'X-Microsoft-OutputFormat': 'audio-24khz-48kbitrate-mono-mp3',
            'User-Agent': 'smoothie-english-bro',
        },
        timeout=30.0,
    )
    if not response.is_success:
        logger.warning('tts_provider_failed provider=azure http_status=%s', response.status_code)
        response.raise_for_status()
    if not response.content:
        logger.warning('tts_no_audio provider=azure')
        return None

    file_name = f'{output_base_name}_0.mp3'
    Path(file_name).write_bytes(response.content)
    logger.info('tts_stream_completed provider=azure audio_bytes=%s', len(response.content))
    return file_name
