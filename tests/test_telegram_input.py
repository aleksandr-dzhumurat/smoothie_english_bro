import os
import unittest
from types import SimpleNamespace
from unittest.mock import AsyncMock, patch

from telegram import Message, Update
from telegram.error import NetworkError
from telegram.ext import Application, ExtBot

with patch.dict(os.environ, {'TG_BOT_TOKEN': '123:test-token'}):
    import app


class TelegramInputTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.telegram = Application.builder().token('123:test-token').updater(None).build()
        with patch.object(ExtBot, 'initialize', new_callable=AsyncMock):
            await self.telegram.initialize()
        with patch.object(app, 'bot_dialog', new_callable=AsyncMock) as dialog, patch.object(
            app, 'narration_command', new_callable=AsyncMock
        ) as narration:
            self.dialog = dialog
            self.narration = narration
            app.register_handlers(self.telegram)
        self.reply = self.enterContext(patch.object(Message, 'reply_text', new_callable=AsyncMock))

    async def asyncTearDown(self):
        with patch.object(ExtBot, 'shutdown', new_callable=AsyncMock):
            await self.telegram.shutdown()

    def update(self, **message_fields):
        return Update.de_json({
            'update_id': 1,
            'message': {
                'message_id': 1, 'date': 0,
                'chat': {'id': 42, 'type': 'private'},
                'from': {'id': 42, 'is_bot': False, 'first_name': 'Test'},
                **message_fields,
            },
        }, self.telegram.bot)

    async def test_warns_and_rejects_attachments_and_captions(self):
        file = {'file_id': 'file', 'file_unique_id': 'unique'}
        for attachment in (
            {'document': file},
            {'photo': [{**file, 'width': 10, 'height': 10}]},
            {'voice': {**file, 'duration': 1}},
        ):
            with self.subTest(attachment=attachment):
                self.reply.reset_mock()
                with self.assertLogs('app', level='INFO') as logs:
                    await self.telegram.process_update(self.update(caption='/narration hi', **attachment))
                self.assertIn('reason=attachment', logs.output[-1])
                self.assertIn('caption_chars=13', logs.output[-1])
                self.assertNotIn('/narration hi', '\n'.join(logs.output))
                self.reply.assert_awaited_once_with(app.ATTACHMENT_WARNING)
        self.dialog.assert_not_called()
        self.narration.assert_not_called()

    async def test_warns_and_rejects_oversized_text_and_narration_command(self):
        long_text = 'x' * (app.MAX_INPUT_LENGTH + 1)
        command = '/narration'
        with self.assertLogs('app', level='INFO') as logs:
            await self.telegram.process_update(self.update(text=long_text))
            await self.telegram.process_update(self.update(
                text=f'{command} {long_text}',
                entities=[{'type': 'bot_command', 'offset': 0, 'length': len(command)}],
            ))
        self.assertIn(f'reason=too_long chars={len(long_text)} limit={app.MAX_INPUT_LENGTH}', '\n'.join(logs.output))
        self.assertEqual(self.reply.await_count, 2)
        for call in self.reply.await_args_list:
            self.assertIn('That text is too long', call.args[0])
        self.dialog.assert_not_called()
        self.narration.assert_not_called()

    async def test_accepts_plain_text_at_the_limit(self):
        await self.telegram.process_update(self.update(text='x' * app.MAX_INPUT_LENGTH))
        self.reply.assert_not_called()
        self.dialog.assert_awaited_once()

    async def test_logs_formatting_and_group_without_message_content(self):
        text = 'Private heading\nBody'
        with self.assertLogs('app', level='INFO') as logs:
            await self.telegram.process_update(self.update(
                chat={'id': -42, 'type': 'group', 'title': 'Private group'}, text=text,
                entities=[{'type': 'bold', 'offset': 0, 'length': 15}],
            ))
        self.assertIn('chat_type=group', logs.output[0])
        self.assertIn('text_entities=bold', logs.output[0])
        self.assertNotIn('Private', logs.output[0])
        self.dialog.assert_awaited_once()

    async def test_logs_group_privacy_from_cached_bot_profile(self):
        for can_read in (True, None):
            application = SimpleNamespace(bot=SimpleNamespace(
                bot=SimpleNamespace(can_read_all_group_messages=can_read),
            ))
            with self.assertLogs('app', level='INFO') as logs:
                await app.log_group_privacy(application)
            self.assertIn(f'telegram_group_privacy enabled={not can_read}', logs.output[0])

    async def test_logs_then_narrates_rich_message_without_regular_text(self):
        prefix = 'Private heading\n\nOpen the guide\n\nFirst item.\n\n'
        excerpt = 'x' * (4114 - len(prefix))
        update = self.update(rich_message={'blocks': [
            {'type': 'heading', 'size': 2, 'text': {'type': 'bold', 'text': 'Private heading'}},
            {'type': 'paragraph', 'text': ['Open ', {'type': 'url', 'text': 'the guide', 'url': 'https://example.com'}]},
            {'type': 'list', 'items': [{'blocks': [{'type': 'paragraph', 'text': 'First item.'}]}]},
            {'type': 'paragraph', 'text': excerpt},
        ]})
        session = {'session_id': 'session', 'session_state': 'narration'}
        with patch.object(app, 'get_session', return_value=session), patch.object(
            app, 'set_session_state', new_callable=AsyncMock
        ) as set_state, patch.object(app, '_generate_and_send_speech', new_callable=AsyncMock) as speech, self.assertLogs(
            'app', level='INFO'
        ) as logs:
            await self.telegram.process_update(update)
        self.assertIn('message_type=rich_message', logs.output[0])
        self.assertIn('rich_message_extracted', logs.output[1])
        self.assertNotIn('Private heading', '\n'.join(logs.output))
        self.assertEqual(speech.await_args.args[2], prefix + excerpt)
        set_state.assert_awaited_once_with('session', 'translate')
        self.dialog.assert_not_called()

    async def test_rejects_oversized_rich_text_and_embedded_attachments(self):
        cases = (
            ([{'type': 'paragraph', 'text': 'x' * (app.MAX_INPUT_LENGTH + 1)}], app.LONG_TEXT_WARNING),
            ([{'type': 'details', 'summary': 'Media', 'blocks': [{'type': 'photo'}]}], app.ATTACHMENT_WARNING),
        )
        with patch.object(app, '_generate_and_send_speech', new_callable=AsyncMock) as speech:
            for blocks, warning in cases:
                with self.subTest(warning=warning):
                    self.reply.reset_mock()
                    await self.telegram.process_update(self.update(rich_message={'blocks': blocks}))
                    self.reply.assert_awaited_once_with(warning)
        speech.assert_not_called()

    async def test_does_not_route_rejected_text_if_warning_fails(self):
        self.reply.side_effect = NetworkError('test failure')
        with self.assertLogs('app', level='ERROR'):
            await self.telegram.process_update(self.update(text='x' * (app.MAX_INPUT_LENGTH + 1)))
        self.dialog.assert_not_called()

    async def test_reaction_does_not_send_previously_saved_long_text_to_ai(self):
        update = Update.de_json({
            'update_id': 2,
            'message_reaction': {
                'chat': {'id': 42, 'type': 'private'}, 'message_id': 1, 'date': 0,
                'old_reaction': [], 'new_reaction': [{'type': 'emoji', 'emoji': '👍'}],
            },
        }, self.telegram.bot)
        stored = {'message_text': 'x' * (app.MAX_INPUT_LENGTH + 1)}
        with patch.object(app, 'get_message_by_id', return_value=stored), patch.object(
            ExtBot, 'send_message', new_callable=AsyncMock
        ) as warning, patch.object(app, 'english_to_russian') as translate, patch.object(
            app, 'generate_speech'
        ) as speech:
            await self.telegram.process_update(update)
        warning.assert_awaited_once_with(chat_id=42, text=app.LONG_TEXT_WARNING)
        translate.assert_not_called()
        speech.assert_not_called()
