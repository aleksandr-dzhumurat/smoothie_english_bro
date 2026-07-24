"""Extract readable text from Telegram's structured Rich Message blocks."""

from collections.abc import Mapping


class RichMessageAttachment(ValueError):
    """The message contains embedded media rather than just text."""


def get_rich_message(message):
    # Older python-telegram-bot versions preserve unknown Bot API fields here.
    native = getattr(message, 'rich_message', None)
    if native is not None:
        return native if isinstance(native, Mapping) else native.to_dict()
    return message.api_kwargs.get('rich_message')


def _inline(value):
    if isinstance(value, str):
        return value
    if isinstance(value, (list, tuple)):
        return ''.join(_inline(part) for part in value)
    if isinstance(value, Mapping):
        return _inline(value.get('text', value.get('alternative_text', value.get('expression'))))
    return ''


def _join(parts, separator='\n\n'):
    return separator.join(part for part in parts if part.strip())


def _block(block):
    kind = block['type']
    if kind in {'photo', 'video', 'document', 'audio', 'animation', 'voice_note', 'collage', 'slideshow', 'map'}:
        raise RichMessageAttachment
    if kind in {'heading', 'paragraph', 'pre', 'footer'}:
        return _inline(block['text'])
    if kind in {'blockquote', 'expandable_blockquote'}:
        return _join([_blocks(block['blocks']), _inline(block.get('credit'))])
    if kind == 'pullquote':
        return _join([_inline(block['text']), _inline(block.get('credit'))])
    if kind == 'details':
        return _join([_inline(block.get('summary')), _blocks(block['blocks'])])
    if kind == 'list':
        return _join((_blocks(item['blocks']) for item in block['items']), '\n')
    if kind == 'table':
        rows = (_join((_inline(cell.get('text')) for cell in row), '; ') for row in block['cells'])
        return _join([_inline(block.get('caption')), _join(rows, '\n')])
    if kind == 'mathematical_expression':
        return _inline(block['expression'])
    if kind in {'divider', 'anchor', 'buttons', 'thinking'}:
        return ''
    raise ValueError('Unsupported Rich Message block')


def _blocks(blocks):
    return _join(_block(block) for block in blocks)


def rich_message_to_text(rich_message) -> str:
    """Flatten display text in reading order, without fetching media or following links."""
    return _blocks(rich_message['blocks']).strip()
