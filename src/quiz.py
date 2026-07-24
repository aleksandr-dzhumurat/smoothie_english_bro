#!/usr/bin/env python3
"""Interactive grammar quiz CLI.

Flow:
    1. read units          (via parse_units.parse_dir)
    2. sample a theme       (a random unit that has answerable questions)
    3. sample a question    (a random multiple-choice question from that theme)
    4. print it, wait for the user's answer
    5. check the answer, show the explanation

Usage:
    python quiz.py                                 # reads the bundled units by default
    python quiz.py --input ./units --theme 12      # stay on one unit
    python quiz.py --input ./units --seed 7        # reproducible sampling

Controls while playing:
    1..N   choose a variant
    s      skip / reveal the answer
    q      quit
"""
from __future__ import annotations

import argparse
import random
import sys
from pathlib import Path
from typing import Optional

from parse_units import DEFAULT_UNITS_DIR, UnitDoc, Quiz, image_question_trigger, parse_dir


# --------------------------------------------------------------------------- data prep

def is_image_question(q: Quiz) -> bool:
    """True if the question depends on a picture/diagram the bot can't show."""
    return image_question_trigger(q) is not None


def _answerable(q: Quiz) -> bool:
    """A question we can actually grade: has variants, a known correct one,
    and no dependency on a visual we cannot display."""
    return (q.correct_index is not None and 1 <= q.correct_index <= len(q.variants)
            and not is_image_question(q))


def build_themes(docs: list[UnitDoc]) -> dict[str, tuple[UnitDoc, list[Quiz]]]:
    """theme label -> (unit doc, list of answerable quizzes)."""
    themes: dict[str, tuple[UnitDoc, list[Quiz]]] = {}
    for d in docs:
        quizzes = [q for q in d.quizzes if _answerable(q)]
        if quizzes:
            label = d.title or f"Unit {d.unit}"
            themes[label] = (d, quizzes)
    return themes


class QuizStore:
    """Load the units once and sample a question from a random theme."""

    def __init__(self, units_dir: Path = DEFAULT_UNITS_DIR) -> None:
        self.themes = build_themes(parse_dir(units_dir))
        if not self.themes:
            raise ValueError(f"no answerable questions found in {units_dir}")
        self.labels = list(self.themes)
        self.total = sum(len(quizzes) for _, quizzes in self.themes.values())
        self._rng = random.Random()

    def sample(self) -> tuple[str, UnitDoc, Quiz]:
        label = self._rng.choice(self.labels)
        doc, quizzes = self.themes[label]
        return label, doc, self._rng.choice(quizzes)

    def shuffled_variants(self, quiz: Quiz) -> tuple[list[str], int]:
        return shuffle_variants(quiz, self._rng)


def shuffle_variants(quiz: Quiz, rng: random.Random) -> tuple[list[str], int]:
    """Return shuffled answer choices and the 1-based position of the correct choice."""
    assert quiz.correct_index is not None
    order = list(range(len(quiz.variants)))
    rng.shuffle(order)
    return [quiz.variants[i] for i in order], order.index(quiz.correct_index - 1) + 1


# --------------------------------------------------------------------------- one round

def ask_question(theme_label: str, doc: UnitDoc, quiz: Quiz, rng: random.Random) -> str:
    """Print one question, read the answer, grade it.

    Returns one of: "correct", "wrong", "skip", "quit".
    """
    shuffled, correct_pos = shuffle_variants(quiz, rng)

    unit_tag = f"Unit {doc.unit}" if doc.unit is not None else "Unit ?"
    print("\n" + "=" * 70)
    print(f"Theme: {theme_label}  ({unit_tag}, question {quiz.number})")
    print("=" * 70)
    print(f"\n{quiz.question}\n")
    for i, variant in enumerate(shuffled, 1):
        print(f"  {i}. {variant}")

    choice = input("\nYour answer (1..%d, s=skip, q=quit): " % len(shuffled)).strip().lower()

    if choice in ("q", "quit"):
        return "quit"
    if choice in ("s", "skip", ""):
        print(f"\nSkipped. Correct answer: {correct_pos}. {shuffled[correct_pos - 1]}")
        _print_explanation(quiz)
        return "skip"

    if not choice.isdigit() or not (1 <= int(choice) <= len(shuffled)):
        print("  (not a valid choice — counted as skipped)")
        print(f"Correct answer: {correct_pos}. {shuffled[correct_pos - 1]}")
        _print_explanation(quiz)
        return "skip"

    picked = int(choice)
    if picked == correct_pos:
        print("\n✅ Correct!")
        _print_explanation(quiz)
        return "correct"

    print(f"\n❌ Not quite. Correct answer: {correct_pos}. {shuffled[correct_pos - 1]}")
    _print_explanation(quiz)
    return "wrong"


def _print_explanation(quiz: Quiz) -> None:
    if quiz.answer:
        print(f"\nWhy: {quiz.answer}")


# --------------------------------------------------------------------------- loop

def run(themes: dict[str, tuple[UnitDoc, list[Quiz]]], pinned: Optional[int], rng: random.Random) -> None:
    labels = list(themes.keys())
    asked = correct = 0

    try:
        while True:
            # 1) sample a theme (or use the pinned one)
            if pinned is not None:
                match = [lbl for lbl, (d, _) in themes.items() if d.unit == pinned]
                if not match:
                    print(f"unit {pinned} has no answerable questions", file=sys.stderr)
                    return
                label = match[0]
            else:
                label = rng.choice(labels)

            doc, quizzes = themes[label]
            # 2) sample a question from that theme
            quiz = rng.choice(quizzes)

            # 3 + 4) print and grade
            result = ask_question(label, doc, quiz, rng)
            if result == "quit":
                break
            if result in ("correct", "wrong"):
                asked += 1
                correct += int(result == "correct")
    except (KeyboardInterrupt, EOFError):
        print()

    if asked:
        print(f"\nScore: {correct}/{asked} ({100 * correct // asked}%)")
    print("Bye!")


# --------------------------------------------------------------------------- CLI

def main(argv: Optional[list[str]] = None) -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("--input", type=Path, default=DEFAULT_UNITS_DIR,
                    help="directory with .md unit files (default: bundled units)")
    ap.add_argument("--theme", type=int, metavar="UNIT", help="stay on a single unit number")
    ap.add_argument("--seed", type=int, help="seed the random sampling (reproducible runs)")
    args = ap.parse_args(argv)

    if not args.input.is_dir():
        ap.error(f"--input must be an existing directory: {args.input}")

    docs = parse_dir(args.input)
    themes = build_themes(docs)
    if not themes:
        ap.error(f"no answerable questions found in {args.input}")

    rng = random.Random(args.seed)
    total_q = sum(len(q) for _, q in themes.values())
    print(f"Loaded {len(themes)} themes, {total_q} questions. Let's practise!")

    run(themes, args.theme, rng)
    return 0


if __name__ == "__main__":
    sys.exit(main())
