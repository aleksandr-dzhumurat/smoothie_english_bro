#!/usr/bin/env python3
"""Parse grammar unit markdown files into Theory / Quiz dataclasses.

Usage:
    python parse_units.py --input ./units            # summary
    python parse_units.py --input ./units --json out.json
    python parse_units.py --input ./units --show 12  # print parsed unit 12

Supported markdown layout (heading levels are detected automatically, so both
the `## Question N / ### Question` style of deeplearning.md and the
`### Question N / #### Question` style of the unit files work):

    # Unit N — Title
    # Theory
    ...
    # Exercises
    ## Book exercises            (optional group heading)
    ### Question 1
    #### Question
    ...
    #### Answer
    ...
    #### Correct variant
    ¯\\_(ツ)_/¯                  (placeholder; real answer is the "(Correct)" variant)
    #### Variants
    1. ...
    2. ... (Correct)
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Iterator, Optional

DEFAULT_UNITS_DIR = Path(__file__).resolve().parents[1] / "english_phone_Interview_preparing" / "units"

CORRECT_MARK = re.compile(r"\s*\(Correct\)\s*$", re.IGNORECASE)
PLACEHOLDER = re.compile(r"^\s*¯\\?_\(ツ\)_/¯\s*$")
QUESTION_HEAD = re.compile(r"^(#{2,4})[ \t]+Question[ \t]+(\d+)[ \t]*\r?$", re.MULTILINE)
VARIANT_LINE = re.compile(r"^\s*(\d+)[.)]\s+(.*\S)\s*$")

# Match references to a specific visual, not incidental phrases like "take photos".
_VISUAL = r"(?:pictures?|photos?|diagrams?|maps?|charts?|figures?|illustrations?)"
_VISUAL_REFERENCE = re.compile("|".join((
    rf"\blook\s+at\s+(?:the|this|these)\s+{_VISUAL}\b",
    rf"\b(?:for|from|in|about|according\s+to)\s+the\s+{_VISUAL}\b",
    rf"\b{_VISUAL}\s+\d+\b",
    rf"\bthe\s+{_VISUAL}\s+(?:above|below|on\s+the\s+(?:right|left)|shows?)\b",
    r"\bshown\s+(?:below|above)\b",
    rf"\beach\s+{_VISUAL}\b",
)), re.IGNORECASE)
_IMAGE_MARKUP = re.compile(r"!\[[^\]\n]*\](?:\([^\n]+\)|\[[^\]\n]*\])|<img\b[^>]*>",
                           re.IGNORECASE)


@dataclass
class Theory:
    unit: Optional[int]
    title: str
    text: str
    sections: dict[str, str] = field(default_factory=dict)  # "## A ..." -> body


@dataclass
class Quiz:
    number: int
    question: str
    answer: str                      # correct answer with explanation
    variants: list[str]              # without the "(Correct)" marker
    correct_variant: Optional[str]   # text of the correct variant (None if no variants)
    correct_index: Optional[int]     # 1-based index into `variants`
    group: Optional[str] = None      # e.g. "Book exercises" / "Extra practice"
    exercise_ref: Optional[str] = None  # e.g. "12.1 (item 2)" when present
    unit: Optional[int] = None
    source: str = ""


@dataclass
class UnitDoc:
    path: str
    unit: Optional[int]
    title: str
    theory: Theory
    quizzes: list[Quiz]


# --------------------------------------------------------------------------- helpers

def _top_sections(md: str) -> Iterator[tuple[str, int, int]]:
    """Yield each level-1 heading and the source offsets of its body."""
    heads = list(re.finditer(r"^# (.+)$", md, flags=re.MULTILINE))
    for i, head in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else len(md)
        yield head.group(1).strip(), head.end(), end


def _sub_blocks(body: str, level: int) -> dict[str, str]:
    """Split `body` by headings of exactly `level` -> {heading: text}."""
    pat = re.compile(rf"^{'#' * level}(?!#)\s+(.+)$", re.MULTILINE)
    parts = pat.split(body)
    blocks: dict[str, str] = {}
    for i in range(1, len(parts), 2):
        blocks[parts[i].strip().lower()] = parts[i + 1].strip()
    return blocks


def _parse_unit_header(title_line: str) -> tuple[Optional[int], str]:
    m = re.match(r"Unit\s+(\d+)\s*[—\-–:]\s*(.*)", title_line)
    if m:
        return int(m.group(1)), m.group(2).strip()
    return None, title_line.strip()


def _parse_variants(block: str) -> tuple[list[str], Optional[str], Optional[int]]:
    variants: list[str] = []
    correct_idx: Optional[int] = None
    for line in block.splitlines():
        m = VARIANT_LINE.match(line)
        if not m:
            # continuation of previous variant
            if variants and line.strip():
                variants[-1] += " " + line.strip()
            continue
        text = m.group(2)
        if CORRECT_MARK.search(text):
            text = CORRECT_MARK.sub("", text).strip()
            correct_idx = len(variants) + 1
        variants.append(text)
    correct = variants[correct_idx - 1] if correct_idx else None
    return variants, correct, correct_idx


def _parse_question_block(number: int, block: str, level: int) -> Quiz:
    """`level` is the heading level of the `Question N` line; inner headings are one deeper."""
    inner = _sub_blocks(block, level + 1)
    question = inner.get("question", "").strip()
    answer = inner.get("answer", "").strip()
    variants, correct, idx = _parse_variants(inner.get("variants", ""))

    # Fallback: explicit "Correct variant" section that is not the placeholder
    cv = inner.get("correct variant", "").strip()
    if correct is None and cv and not PLACEHOLDER.match(cv):
        correct = cv
        if cv in variants:
            idx = variants.index(cv) + 1

    ref = None
    m = re.search(r"\*\*Exercise\s+([\d.]+(?:\s*\(item[^)]*\))?)\*\*", question)
    if m:
        ref = m.group(1)

    return Quiz(number=number, question=question, answer=answer, variants=variants,
                correct_variant=correct, correct_index=idx, exercise_ref=ref)


def _iter_questions(exercises_body: str) -> Iterator[tuple[Quiz, int, int]]:
    """Yield parsed quizzes and their source spans relative to the exercises body."""
    heads = list(QUESTION_HEAD.finditer(exercises_body))
    if not heads:
        return
    q_level = len(heads[0].group(1))
    # group headings are one level above the question headings (if any)
    group_pat = re.compile(rf"^{'#' * (q_level - 1)}[ \t]+(.+)$", re.MULTILINE)
    groups = iter(group_pat.finditer(exercises_body)) if q_level > 2 else iter(())
    next_group = next(groups, None)
    group = None

    for i, h in enumerate(heads):
        while next_group is not None and next_group.start() < h.start():
            group = next_group.group(1).strip()
            next_group = next(groups, None)
        end = heads[i + 1].start() if i + 1 < len(heads) else len(exercises_body)
        if next_group is not None:
            end = min(end, next_group.start())
        block = exercises_body[h.end():end]
        block = re.sub(r"\n---\s*$", "\n", block.rstrip() + "\n")  # drop trailing separator
        q = _parse_question_block(int(h.group(2)), block, len(h.group(1)))
        q.group = group
        yield q, h.start(), end


# --------------------------------------------------------------------------- public API

def image_question_trigger(q: Quiz) -> Optional[str]:
    """Return the text or image markup that makes this quiz depend on a visual."""
    match = _VISUAL_REFERENCE.search(q.question)
    if match:
        return match.group(0)
    for text in (q.question, *q.variants):
        match = _IMAGE_MARKUP.search(text)
        if match:
            return match.group(0)
    return None


def parse_markdown(md: str, source: str = "") -> UnitDoc:
    doc, _ = parse_markdown_with_spans(md, source)
    return doc


def parse_markdown_with_spans(md: str, source: str = "") -> tuple[UnitDoc, list[tuple[int, int]]]:
    """Return the parsed unit and one Markdown source span per quiz, in quiz order."""
    title_line = ""
    theory_body = ""
    exercise_start = exercise_end = 0
    for heading, start, end in _top_sections(md):
        h = heading.lower()
        if h == "theory":
            theory_body = md[start:end]
        elif h in ("exercises", "execises", "exercise"):
            exercise_start, exercise_end = start, end
        elif heading and not title_line:
            title_line = heading
            # deeplearning.md style: questions live directly under the title heading
            if exercise_start == exercise_end and QUESTION_HEAD.search(md, start, end):
                exercise_start, exercise_end = start, end

    unit, title = _parse_unit_header(title_line)
    theory = Theory(unit=unit, title=title, text=theory_body.strip(),
                    sections=_sub_blocks(theory_body, 2))

    quizzes: list[Quiz] = []
    spans: list[tuple[int, int]] = []
    for q, start, end in _iter_questions(md[exercise_start:exercise_end]):
        q.unit, q.source = unit, source
        quizzes.append(q)
        spans.append((exercise_start + start, exercise_start + end))

    return UnitDoc(path=source, unit=unit, title=title, theory=theory, quizzes=quizzes), spans


def parse_file(path: Path) -> UnitDoc:
    return parse_markdown(path.read_text(encoding="utf-8"), source=str(path))


def unit_files(directory: Path) -> list[Path]:
    return sorted(p for p in directory.iterdir() if p.suffix.lower() == ".md" and p.is_file())


def parse_dir(directory: Path) -> list[UnitDoc]:
    return [parse_file(p) for p in unit_files(directory)]


# --------------------------------------------------------------------------- CLI

def _show(doc: UnitDoc) -> None:
    print(f"== {doc.path}\nUnit {doc.unit}: {doc.title}")
    print(f"Theory: {len(doc.theory.text.split())} words, sections: {list(doc.theory.sections)}")
    for q in doc.quizzes:
        print(f"\n[{q.number}] ({q.group}) {q.exercise_ref or ''}\n  Q: {q.question[:160]!r}")
        for i, v in enumerate(q.variants, 1):
            print(f"    {'*' if i == q.correct_index else ' '} {i}. {v}")
        print(f"  A: {q.answer[:160]!r}")


def main(argv: Optional[list[str]] = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--input", type=Path, default=DEFAULT_UNITS_DIR, help="directory with .md unit files")
    ap.add_argument("--json", type=Path, help="write parsed data to this JSON file")
    ap.add_argument("--show", type=int, metavar="UNIT", help="pretty-print one parsed unit")
    ap.add_argument("--strict", action="store_true", help="exit 1 if any quiz lacks a correct variant")
    args = ap.parse_args(argv)

    if not args.input.is_dir():
        ap.error(f"--input must be an existing directory: {args.input}")

    docs = parse_dir(args.input)
    if not docs:
        ap.error(f"no .md files found in {args.input}")

    problems = [(d.path, q.number) for d in docs for q in d.quizzes
                if q.variants and q.correct_variant is None]
    total_q = sum(len(d.quizzes) for d in docs)
    print(f"files: {len(docs)}  quizzes: {total_q}  "
          f"with variants: {sum(1 for d in docs for q in d.quizzes if q.variants)}  "
          f"missing correct: {len(problems)}")
    for p, n in problems[:20]:
        print(f"  missing correct variant: {p} question {n}")

    if args.show is not None:
        for d in docs:
            if d.unit == args.show:
                _show(d)
                break
        else:
            print(f"unit {args.show} not found", file=sys.stderr)

    if args.json:
        args.json.write_text(json.dumps([asdict(d) for d in docs], ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"wrote {args.json}")

    return 1 if (args.strict and problems) else 0


if __name__ == "__main__":
    sys.exit(main())
