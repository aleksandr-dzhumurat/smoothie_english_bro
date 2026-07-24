import math
import os
import shutil
import struct
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch
from xml.etree import ElementTree

import httpx
from google.genai import errors

import azure_tts
import gemini_adapter


class AzureSpeechTests(unittest.TestCase):
    def test_defaults_to_british_female_voice_and_slow_speed(self):
        url = 'https://uksouth.tts.speech.microsoft.com/cognitiveservices/v1'
        response = httpx.Response(200, content=b'mp3 audio', request=httpx.Request('POST', url))
        with tempfile.TemporaryDirectory() as directory, patch.dict(os.environ, {
            'AZURE_SPEECH_KEY': 'test-key',
            'AZURE_SPEECH_REGION': 'uksouth',
        }), patch('azure_tts.httpx.post', return_value=response) as post:
            text = 'Fish & chips <please>'
            path = azure_tts.generate_speech(text, f'{directory}/speech')
            self.assertEqual(path, f'{directory}/speech_0.mp3')
            self.assertEqual(Path(path).read_bytes(), b'mp3 audio')

        self.assertEqual(post.call_args.args, (url,))
        request = post.call_args.kwargs
        self.assertEqual(request['headers']['X-Microsoft-OutputFormat'], 'audio-24khz-48kbitrate-mono-mp3')
        ssml = ElementTree.fromstring(request['content'])
        self.assertEqual(ssml.attrib['{http://www.w3.org/XML/1998/namespace}lang'], 'en-GB')
        self.assertEqual(ssml[0].attrib['name'], 'en-GB-SoniaNeural')
        self.assertEqual(ssml[0][0].attrib['rate'], '-30%')
        self.assertEqual(ssml[0][0].text, text)

    def test_rejects_non_english_voices(self):
        with self.assertRaises(ValueError):
            azure_tts.generate_speech('Hello', 'speech', voice='fr-FR-DeniseNeural')


class GeminiSpeechTests(unittest.TestCase):
    @patch('gemini_adapter.subprocess.run', side_effect=FileNotFoundError)
    @patch('gemini_adapter.genai.Client')
    def test_requests_slow_verbatim_narration_even_without_ffmpeg(self, client, ffmpeg):
        stream = client.return_value.models.generate_content_stream
        transcript = 'Hello.\nPlease read this exactly.'
        chunk = MagicMock(usage_metadata=None)
        pcm = b'\x00\x01\x00\xff'
        chunk.parts[0].inline_data.data = pcm
        chunk.parts[0].inline_data.mime_type = 'audio/L16;codec=pcm;rate=24000'
        stream.return_value = iter([chunk])

        with tempfile.TemporaryDirectory() as directory, self.assertLogs('gemini_adapter', level='WARNING'):
            path = gemini_adapter.generate_speech(transcript, f'{directory}/speech')
            self.assertEqual(path, f'{directory}/speech_0.wav')
            self.assertEqual(Path(path).read_bytes()[44:], pcm)

        prompt = stream.call_args.kwargs['contents'][0].parts[0].text
        instruction, spoken_text = prompt.split('\n\nTranscript:\n', 1)
        self.assertIn('70 percent of your normal speaking pace', instruction)
        self.assertIn('verbatim', instruction)
        self.assertEqual(spoken_text, transcript)
        self.assertNotIn('-af', ffmpeg.call_args.args[0])

    @unittest.skipUnless(shutil.which('ffmpeg'), 'FFmpeg is not installed')
    @patch('gemini_adapter.genai.Client')
    def test_mp3_encoding_preserves_gemini_audio_duration_and_pitch(self, client):
        sample_rate = 24000
        pitch = 440
        duration = 2
        samples = [
            int(10000 * math.sin(2 * math.pi * pitch * i / sample_rate))
            for i in range(sample_rate * duration)
        ]
        chunk = MagicMock(usage_metadata=None)
        chunk.parts[0].inline_data.data = struct.pack(f'<{len(samples)}h', *samples)
        chunk.parts[0].inline_data.mime_type = 'audio/L16;codec=pcm;rate=24000'
        client.return_value.models.generate_content_stream.return_value = iter([chunk])

        with tempfile.TemporaryDirectory() as directory:
            path = gemini_adapter.generate_speech('Hello', f'{directory}/speech')
            self.assertEqual(path, f'{directory}/speech_0.mp3')
            decoded = subprocess.run(
                ['ffmpeg', '-loglevel', 'error', '-i', path, '-ar', str(sample_rate),
                 '-f', 's16le', 'pipe:1'],
                capture_output=True, check=True, timeout=10,
            ).stdout

        played = struct.unpack(f'<{len(decoded) // 2}h', decoded)
        self.assertAlmostEqual(len(played) / sample_rate, duration, delta=0.1)
        middle_second = played[sample_rate // 2:3 * sample_rate // 2]
        positive_crossings = sum(a <= 0 < b for a, b in zip(middle_second, middle_second[1:]))
        self.assertAlmostEqual(positive_crossings, pitch, delta=5)


class GeminiSpeechFallbackTests(unittest.TestCase):
    @patch('gemini_adapter.azure_tts.generate_speech')
    @patch('gemini_adapter._generate_gemini_speech', return_value='gemini.wav')
    def test_uses_gemini_when_available(self, gemini, azure):
        self.assertEqual(gemini_adapter.generate_speech('Hello', 'speech'), 'gemini.wav')
        gemini.assert_called_once_with('Hello', 'speech')
        azure.assert_not_called()

    @patch('gemini_adapter.azure_tts.generate_speech', return_value='azure.mp3')
    @patch('gemini_adapter.genai.Client')
    def test_falls_back_when_stream_hits_limit(self, client, azure):
        def quota_limited_stream(**kwargs):
            chunk = MagicMock(usage_metadata=None)
            chunk.parts[0].inline_data.data = b'partial audio'
            yield chunk
            raise errors.ClientError(429, {'error': {'status': 'RESOURCE_EXHAUSTED'}})

        client.return_value.models.generate_content_stream.side_effect = quota_limited_stream
        with tempfile.TemporaryDirectory() as directory, self.assertLogs('gemini_adapter', level='WARNING'):
            output_base = f'{directory}/speech'
            self.assertEqual(gemini_adapter.generate_speech('Hello', output_base), 'azure.mp3')
            self.assertEqual(list(Path(directory).iterdir()), [])
        azure.assert_called_once_with('Hello', output_base)

    @patch('gemini_adapter.azure_tts.generate_speech')
    @patch('gemini_adapter._generate_gemini_speech')
    def test_does_not_fall_back_on_other_gemini_errors(self, gemini, azure):
        error = errors.ClientError(403, {'error': {'status': 'PERMISSION_DENIED'}})
        gemini.side_effect = error
        with self.assertRaises(errors.ClientError) as raised:
            gemini_adapter.generate_speech('Hello', 'speech')
        self.assertIs(raised.exception, error)
        azure.assert_not_called()
