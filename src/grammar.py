"""Telegram handlers for the multiple-choice grammar quiz."""

import html
import logging
import os
import re
import uuid
from dataclasses import dataclass
from pathlib import Path

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Message, Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes

from db import get_grammar_stats, save_grammar_attempt
from parse_units import DEFAULT_UNITS_DIR, Quiz
from quiz import QuizStore

log = logging.getLogger(__name__)
ANSWER_PATTERN = r"^grammar_answer:([0-9a-f]{32}):([1-9][0-9]*)$"
_EMPHASIS = re.compile(r"\*\*(.+?)\*\*|(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", re.DOTALL)
_OPTIONS = re.compile(r"^([^\n]*?\bOptions:)\s*([^\n]+)$", re.MULTILINE)
_OPT_SPLIT = re.compile(r"\s*\(([a-z])\)\s*")


def md_to_html(text: str) -> str:
    """Escape unit text before converting its light Markdown emphasis."""
    return _EMPHASIS.sub(
        lambda m: f"<b>{m[1]}</b>" if m[1] else f"<i>{m[2]}</i>",
        html.escape(text, quote=False),
    )


def question_to_html(text: str) -> str:
    def expand_options(match: re.Match) -> str:
        parts = _OPT_SPLIT.split(match[2])
        if len(parts) < 5 or parts[0].strip():
            return match[0]
        options = (f"  <b>({parts[i]})</b> {parts[i + 1].strip()}"
                   for i in range(1, len(parts), 2))
        return match[1] + "\n" + "\n".join(options)

    # Expand matching exercises, then set off the final fill-in prompt.
    body = _OPTIONS.sub(expand_options, md_to_html(text))
    return re.sub(r"\n+([^\n]*(?:→|______)[^\n]*)$", r"\n\n👉 <b>\1</b>", body)


@dataclass
class PendingQuestion:
    token: str
    message_id: int
    theme: str
    quiz: Quiz
    variants: list[str]
    correct: int
    rendered: str


def load_grammar_store() -> QuizStore | None:
    try:
        store = QuizStore(Path(os.environ.get("UNITS_DIR", DEFAULT_UNITS_DIR)))
    except (OSError, ValueError) as exc:
        log.warning("Grammar questions not loaded: %s", exc)
        return None
    log.info("Loaded %d grammar themes and %d questions", len(store.labels), store.total)
    return store


async def grammar_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.effective_message
    if message is None or context.user_data is None:
        return
    store = context.bot_data.get("grammar_store")
    if store is None:
        await message.reply_text("Grammar questions are unavailable right now.")
        return

    theme, doc, quiz = store.sample()
    variants, correct = store.shuffled_variants(quiz)
    token = uuid.uuid4().hex
    options = "\n".join(f"<b>{i}.</b> {md_to_html(variant)}"
                        for i, variant in enumerate(variants, 1))
    unit = doc.unit if doc.unit is not None else "?"
    rendered = (f"📖 <b>{md_to_html(theme)}</b> <i>(Unit {unit}, Q{quiz.number})</i>\n\n"
                f"{question_to_html(quiz.question)}\n\n{options}")
    buttons = [[InlineKeyboardButton(str(i), callback_data=f"grammar_answer:{token}:{i}")]
               for i in range(1, len(variants) + 1)]
    sent = await message.reply_text(
        rendered, parse_mode=ParseMode.HTML, reply_markup=InlineKeyboardMarkup(buttons),
    )
    pending = context.user_data.setdefault("grammar_pending", {})
    pending[sent.chat_id] = PendingQuestion(token, sent.message_id, theme, quiz, variants, correct, rendered)


async def grammar_answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    message = query.message
    token, picked = context.matches[0][1], int(context.matches[0][2])
    pending = context.user_data.get("grammar_pending", {})
    state = pending.get(message.chat_id) if isinstance(message, Message) else None
    if (state is None or state.token != token or state.message_id != message.message_id
            or not 1 <= picked <= len(state.variants)):
        await query.answer("This question isn't active for you. Tap grammar for a new one.", show_alert=True)
        return

    await save_grammar_attempt(token, query.from_user.id, state.theme, state.quiz.unit,
                               state.quiz.number, picked, state.correct)
    pending.pop(message.chat_id, None)
    await query.answer()

    chosen = md_to_html(state.variants[picked - 1])
    if picked == state.correct:
        verdict = f"✅ <b>Correct!</b> You chose <b>{picked}.</b> {chosen}"
    else:
        correct_text = md_to_html(state.variants[state.correct - 1])
        verdict = (f"❌ <b>Not quite.</b> You chose <b>{picked}.</b> {chosen}\n"
                   f"Correct answer: <b>{state.correct}.</b> {correct_text}")
    explanation = f"\n\n💡 {md_to_html(state.quiz.answer)}" if state.quiz.answer else ""
    result = verdict + explanation
    combined = f"{state.rendered}\n\n———\n{result}"
    if len(combined) <= 4096:
        await query.edit_message_text(combined, parse_mode=ParseMode.HTML, reply_markup=None)
    else:
        await query.edit_message_reply_markup(reply_markup=None)
        await message.reply_text(result, parse_mode=ParseMode.HTML)


async def stats_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    message = update.effective_message
    if user is None or message is None:
        return
    answered, correct = await get_grammar_stats(user.id)
    accuracy = f"{correct / answered:.0%}" if answered else "—"
    await message.reply_text(
        f"📊 <b>Grammar stats</b>\nAnswered: {answered}\nCorrect: {correct}\nAccuracy: {accuracy}",
        parse_mode=ParseMode.HTML,
    )
