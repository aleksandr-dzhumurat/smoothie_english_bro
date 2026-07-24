import json
import os
import random
import re
import zlib
from dataclasses import dataclass
from typing import Iterable, Iterator, Optional

from gemini_adapter import generate_text


def load_json(json_path):
    if not os.path.exists(json_path):
        return {}
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def dump_json(data, quize_db_path):
    with open(quize_db_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def load_jsonl(jsonl_path):
    if not os.path.exists(jsonl_path):
        return []
    with open(jsonl_path, 'r', encoding='utf-8') as f:
        return [json.loads(line) for line in f if line.strip()]

def append_jsonl(record, jsonl_path):
    with open(jsonl_path, 'a', encoding='utf-8') as f:
        f.write(json.dumps(record, ensure_ascii=False) + '\n')

def get_file_path(file_name):
    current_file_path = os.path.abspath(__file__)
    current_dir = os.path.dirname(current_file_path)
    file_path = os.path.join(current_dir, file_name)
    return file_path

def create_translator(source_lang="English", target_lang="Russian"):
    if source_lang == target_lang == 'English':
        system_message = """
            You are a professional translator specializing in corporate communications. Your task is to:

            Critical: if input text is a question, then just fix errors in the original message, do not answer.
            
            If input text is not a question, then do the following:
            
            1. First, provide an English translation with just fixing errors in the original message.
            2. Then, provide 3 alternative phrasings of the translated text, maintaining the same professional tone but using different vocabulary and sentence structures
            3. Each alternative should convey the same meaning but use different expressions common in business communication
            4. Ensure all versions maintain a formal, professional tone suitable for corporate environments

            Format your response as follows:

            PRIMARY TRANSLATION:
            > [Your main translation in polished corporate English]

            ALTERNATIVE PHRASINGS:
            > [First alternative phrasing]
            > [Second alternative phrasing]

            Remember to:
            - Use contemporary business vocabulary
            - Maintain consistency in tone across all versions
            - Ensure each alternative offers a fresh perspective while preserving the original meaning
            - Keep the language clear and accessible for international business audiences
        """
    else:
        system_message = f"""You are a professional translator from {source_lang} to {target_lang}.
    Translate the input text into {target_lang} maintaining the original meaning, tone, and formatting.
    Provide ONLY the translation without explanations, notes, or original text unless specifically requested.
    For specialized terminology, use the appropriate {target_lang} domain-specific terms."""

    def translate_text(user_prompt):
        return generate_text(system_message, user_prompt)

    return translate_text


BEHAVIORAL_ANSWERS_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    'english_phone_Interview_preparing', 'behavioral_answers.md',
)

# `#` and `##` headings delimit questions. Only these two `###` headings split their content.
_SECTION_HEADING_RE = re.compile(r'^(#{1,2})\s+(.+?)\s*$')
_ANSWER_HEADING_RE = re.compile(r'^###\s+(Ideal answer|Hint)\s*$', re.IGNORECASE)
_SEPARATOR_LINES = {'', '---', '***', '___'}  # blank lines and horizontal rules


@dataclass(frozen=True)
class LearnQuestion:
    """An interview question, its recall cue, and its prepared answer in Markdown."""
    id: int
    title: str
    ideal_answer: str
    hint: str = ''


def _clean_body(lines):
    """Join section lines, dropping blank lines and `---` separators at both ends."""
    start, end = 0, len(lines)
    while start < end and lines[start].strip() in _SEPARATOR_LINES:
        start += 1
    while end > start and lines[end - 1].strip() in _SEPARATOR_LINES:
        end -= 1
    return '\n'.join(lines[start:end])


class QuestionsDB:
    """In-memory list of LearnQuestion items with random sampling."""

    def __init__(self, questions: Iterable[LearnQuestion] = ()):
        self._questions = list(questions)

    def __len__(self) -> int:
        return len(self._questions)

    def __iter__(self) -> Iterator[LearnQuestion]:
        return iter(self._questions)

    def get(self, question_id: Optional[int]) -> Optional[LearnQuestion]:
        """Return the question with this id, or None if there isn't one."""
        return next((q for q in self._questions if q.id == question_id), None)

    def get_by_title(self, title: str) -> Optional[LearnQuestion]:
        """Return the question with this exact heading text, or None if there isn't one."""
        return next((q for q in self._questions if q.title == title), None)

    @classmethod
    def from_md(cls, md_path: str = BEHAVIORAL_ANSWERS_PATH) -> 'QuestionsDB':
        """Turn every `##` section of a Markdown file into a LearnQuestion.

        `### Hint` and `### Ideal answer` can appear in either order. For older
        entries, text before the first subsection is the fallback ideal answer.
        IDs are based on the title, so editing either subsection doesn't change them.
        """
        with open(md_path, 'r', encoding='utf-8') as f:
            lines = f.read().splitlines()

        sections: list[tuple[str, dict[str, list[str]]]] = []
        current: Optional[dict[str, list[str]]] = None
        field = 'legacy'
        in_fence = False
        for line in lines:
            if line.lstrip().startswith(('```', '~~~')):
                in_fence = not in_fence
            match = None if in_fence else _SECTION_HEADING_RE.match(line)
            if match:
                # A `#` heading only closes the current section; text under it is skipped.
                current = None
                if len(match.group(1)) == 2:
                    field = 'legacy'
                    current = {field: []}
                    sections.append((match.group(2), current))
            elif current is not None:
                subsection = None if in_fence else _ANSWER_HEADING_RE.match(line)
                if subsection:
                    field = subsection.group(1).lower()
                    current.setdefault(field, [])
                else:
                    current[field].append(line)

        questions = []
        used_ids = set()
        seen_title_counts = {}
        for title, fields in sections:
            ideal_answer = _clean_body(fields.get('ideal answer', fields['legacy']))
            if not ideal_answer:
                continue
            hint = ' '.join(_clean_body(fields.get('hint', [])).split())
            count = seen_title_counts.get(title, 0) + 1
            seen_title_counts[title] = count

            if count == 1:
                question_id = zlib.crc32(title.encode('utf-8'))
            else:
                print(
                    f"Warning: duplicate heading {title!r} in {md_path} "
                    f"(occurrence #{count}); generating a unique id"
                )
                question_id = zlib.crc32(f"{title}#{count}".encode('utf-8'))

            while question_id in used_ids:
                question_id = (question_id + 1) & 0xFFFFFFFF

            used_ids.add(question_id)
            questions.append(LearnQuestion(id=question_id, title=title, ideal_answer=ideal_answer, hint=hint))
        return cls(questions)

    def sample(self, exclude_ids: Optional[Iterable[int]] = None) -> LearnQuestion:
        """Return one random question whose id is not in `exclude_ids`.

        Raises ValueError when every question is excluded (or there are none).
        """
        excluded = set(exclude_ids or ())
        candidates = [q for q in self._questions if q.id not in excluded]
        if not candidates:
            raise ValueError(f'No questions left to sample ({len(self._questions)} total, all excluded)')
        return random.choice(candidates)
