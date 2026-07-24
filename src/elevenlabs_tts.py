import hashlib
import os
import re
import shutil
import sys

import httpx
from dotenv import load_dotenv
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs
from elevenlabs.core.api_error import ApiError

from utils import QuestionsDB, append_jsonl, load_jsonl

load_dotenv()

QUESTION_TITLE = 'Can you discuss navigating a project with a diverse, multicultural team?'

# Speech speed multiplier, 0.7 (slowest) to 1.2 (fastest), 1.0 = voice default.
SPEED = 0.85

AUDIO_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    'data', 'audio',
)

LOG_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    'data', 'log.jsonl',
)

HUMAN_READABLE_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    'data', 'human_readable',
)


def list_voices():
    """Print every voice available to this key: id, category and name.

    Uses the plain /v1/voices endpoint because client.voices.get_all() needs the
    voices_read permission, which restricted keys (TTS-only) don't have.
    """
    response = httpx.get(
        'https://api.elevenlabs.io/v1/voices',
        headers={'xi-api-key': os.environ['ELEVENLABS_API_KEY']},
    )
    response.raise_for_status()
    for voice in response.json()['voices']:
        print(f'{voice["voice_id"]} | {voice["category"]:<8} | {voice["name"]}')


def log_run(title: str, chars_consumed: int, file_hash: str, is_cache: bool) -> None:
    """Append one run record to data/log.jsonl (append-only, keeps all previous runs)."""
    append_jsonl(
        {
            'title': title,
            'chars_consumed': chars_consumed,
            'file_hash': file_hash,
            'is_cache': is_cache,
        },
        LOG_PATH,
    )


def tts_to_file(title: str, body: str) -> None:
    """Synthesize body and save it as data/audio/<sha256(body)>.mp3, skipping cached texts."""
    os.makedirs(AUDIO_DIR, exist_ok=True)
    # Speed is part of the cache key, so changing SPEED regenerates the audio
    # instead of reusing files synthesized at the old speed.
    file_hash = hashlib.sha256(f'speed={SPEED}\n{body}'.encode('utf-8')).hexdigest()
    output_path = os.path.join(AUDIO_DIR, file_hash + '.mp3')
    if os.path.exists(output_path):
        print(f'{output_path} already exists, skipping the API call')
        log_run(title, 0, file_hash, is_cache=True)
        return

    client = ElevenLabs(api_key=os.environ['ELEVENLABS_API_KEY'])
    with client.text_to_speech.with_raw_response.convert(
        text=body,
        voice_id=os.environ.get('ELEVENLABS_VOICE_ID', 'XrExE9yKIg1WjnnlVkGX'),  # Matilda, premade: free tier can't use library voices
        voice_settings=VoiceSettings(speed=SPEED),
    ) as response:
        # chars consumed by this request, from the ElevenLabs response headers
        char_cost = response.headers.get('character-cost')
        print(f'character-cost: {char_cost} chars')
        print(f'request-id: {response.headers.get("request-id")}, trace-id: {response.headers.get("x-trace-id")}')
        audio_data = b''.join(response.data)
    print(f'speed: {SPEED}')

    with open(output_path, 'wb') as f:
        f.write(audio_data)
    print(f'Saved {len(audio_data)} bytes to {output_path}')
    log_run(title, int(char_cost), file_hash, is_cache=False)


def is_quota_exceeded(e: ApiError) -> bool:
    """True when the API rejected the call because the text doesn't fit the remaining quota."""
    detail = e.body.get('detail') if isinstance(e.body, dict) else None
    return e.status_code == 401 and isinstance(detail, dict) and detail.get('code') == 'quota_exceeded'


def interactive(autoconfirm: bool = False) -> None:
    """Walk through all questions one by one, offering to generate audio for each.

    On quota_exceeded the smallest body that failed is remembered: questions at or
    above that size are skipped without an API call (they would need even more
    credits), while smaller ones are still tried.
    """
    questions_db = QuestionsDB.from_md()
    quota_char_limit = None  # smallest body size that failed with quota_exceeded
    for question in questions_db:
        answer_length = len(question.ideal_answer)
        print(f'\n{question.title} ({answer_length} chars)')
        if quota_char_limit is not None and answer_length >= quota_char_limit:
            print(f'Too big for the remaining quota (>= {quota_char_limit} chars), skipping without an API call')
            continue
        if autoconfirm:
            answer = 'y'
        else:
            try:
                answer = input('Generate audio? [y/N] ')
            except (EOFError, KeyboardInterrupt):
                print('\nBye.')
                return
        if answer.strip().lower() != 'y':
            print('Skipped.')
            continue
        try:
            tts_to_file(question.title, question.ideal_answer)
        except ApiError as e:
            if is_quota_exceeded(e):
                quota_char_limit = answer_length if quota_char_limit is None else min(quota_char_limit, answer_length)
                print(f'Quota exceeded, skipped ({answer_length} chars); from now on nothing >= {quota_char_limit} chars is tried')
            else:
                raise


def save_human_readable() -> None:
    """Copy every generated audio to data/human_readable, with the question title in the name.

    Reads data/log.jsonl to map each file hash to its title; the latest run for a
    hash wins. On a name clash (same title, different bodies) the hash is appended.
    """
    os.makedirs(HUMAN_READABLE_DIR, exist_ok=True)
    title_by_hash = {record['file_hash']: record['title'] for record in load_jsonl(LOG_PATH)}

    used_names = set()
    copied = 0
    for file_hash, title in title_by_hash.items():
        src = os.path.join(AUDIO_DIR, file_hash + '.mp3')
        if not os.path.exists(src):
            continue
        name = _safe_file_name(title) + '.mp3'
        if name in used_names:  # same title for two different bodies
            name = _safe_file_name(title) + f'_-_' + file_hash[:8] + '.mp3'
        used_names.add(name)
        shutil.copy2(src, os.path.join(HUMAN_READABLE_DIR, name))
        copied += 1
    print(f'Copied {copied} file(s) to {HUMAN_READABLE_DIR}')


def _safe_file_name(text: str) -> str:
    """Strip characters the filesystem dislikes, collapse whitespace, lowercase, and replace spaces with underscores."""
    cleaned = re.sub(r'[\\/:*?"<>|\r\n\t]+', ' ', text)
    cleaned = re.sub(r'\s+', ' ', cleaned).strip(' .')
    cleaned = cleaned.lower().replace(' ', '_')
    return cleaned[:100] or 'untitled'


def main():
    args = sys.argv[1:]
    if '--list-voices' in args:
        list_voices()
        return
    if '--human-readable' in args:
        save_human_readable()
        return
    if '--interactive' in args:
        interactive(autoconfirm='--autoconfirm' in args)
        return

    questions_db = QuestionsDB.from_md()
    question = questions_db.get_by_title(QUESTION_TITLE)
    if question is None:
        raise SystemExit(f'Question not found: {QUESTION_TITLE}')
    body = question.ideal_answer
    print(f'Question: {question.title} ({len(body)} chars of notes)')

    tts_to_file(question.title, body)


if __name__ == '__main__':
    main()
