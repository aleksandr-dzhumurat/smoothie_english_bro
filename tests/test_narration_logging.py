import os
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import AsyncMock, patch

from telegram.error import BadRequest, NetworkError

with patch.dict(os.environ, {'TG_BOT_TOKEN': '123:test-token'}):
    import app


class NarrationLoggingTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.waiting = SimpleNamespace(edit_text=AsyncMock(), delete=AsyncMock())
        self.reply = AsyncMock(return_value=self.waiting)
        self.send_audio = AsyncMock(return_value=SimpleNamespace(message_id=15))
        self.update = SimpleNamespace(
            update_id=12,
            effective_chat=SimpleNamespace(id=42),
            effective_message=SimpleNamespace(reply_text=self.reply),
        )
        self.context = SimpleNamespace(bot=SimpleNamespace(send_audio=self.send_audio))

    def synthesize(self, text, output_base):
        path = Path(f'{output_base}.mp3')
        path.write_bytes(b'mp3 fixture')
        return str(path)

    async def test_logs_successful_upload(self):
        with patch.object(app, 'generate_speech', side_effect=self.synthesize), self.assertLogs('app', 'INFO') as logs:
            await app._generate_and_send_speech(self.update, self.context, 'private sentence')
        self.assertIn('narration_upload_started update=12 format=.mp3', '\n'.join(logs.output))
        self.assertIn('narration_delivered update=12 audio_message=15', '\n'.join(logs.output))
        self.assertNotIn('private sentence', '\n'.join(logs.output))
        self.waiting.delete.assert_awaited_once()

    async def test_logs_upload_failure_without_exception_payload(self):
        self.send_audio.side_effect = BadRequest('private exception payload')
        with patch.object(app, 'generate_speech', side_effect=self.synthesize), self.assertLogs('app', 'ERROR') as logs:
            await app._generate_and_send_speech(self.update, self.context, 'private sentence')
        self.assertIn('stage=telegram_upload error_type=BadRequest', '\n'.join(logs.output))
        self.assertNotIn('private exception payload', '\n'.join(logs.output))
        self.waiting.edit_text.assert_awaited_once()

    async def test_logs_initial_telegram_failure_without_starting_synthesis(self):
        self.reply.side_effect = NetworkError('private exception payload')
        with patch.object(app, 'generate_speech') as speech, self.assertLogs('app', 'ERROR') as logs:
            await app._generate_and_send_speech(self.update, self.context, 'private sentence')
        self.assertIn('stage=send_waiting_message error_type=NetworkError', '\n'.join(logs.output))
        speech.assert_not_called()
