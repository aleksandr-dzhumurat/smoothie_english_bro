import sqlite3
import time
import uuid
import aiosqlite


DB_PATH = "/srv/src/bot_messages.db"

async def setup_database():
    """Initialize the database with necessary tables."""
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            message_id INTEGER NOT NULL,
            chat_id INTEGER NOT NULL,
            user_id INTEGER NOT NULL,
            message_text TEXT NOT NULL,
            timestamp INTEGER NOT NULL,
            reply_to_message_id INTEGER,
            session_id TEXT,
            PRIMARY KEY (chat_id, message_id)
        )
        ''')
        
        # Create reactions table to track reactions
        await db.execute('''
        CREATE TABLE IF NOT EXISTS reactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            message_id INTEGER NOT NULL,
            user_id INTEGER NOT NULL,
            emoji TEXT NOT NULL,
            timestamp INTEGER NOT NULL,
            FOREIGN KEY (message_id) REFERENCES messages (message_id)
        )
        ''')

        # Try to add reply_to_message_id column if it doesn't exist (for existing databases)
        try:
            await db.execute("ALTER TABLE messages ADD COLUMN reply_to_message_id INTEGER")
        except:
            pass
        try:
            await db.execute("ALTER TABLE messages ADD COLUMN session_id TEXT")
        except:
            pass

        await db.execute('''
        CREATE TABLE IF NOT EXISTS translations (
            english_message TEXT NOT NULL,
            russian_message TEXT NOT NULL
        )
        ''')

        await db.execute('''
        CREATE TABLE IF NOT EXISTS sessions (
            session_id TEXT PRIMARY KEY,
            user_id INTEGER NOT NULL,
            created_at INTEGER NOT NULL,
            session_state TEXT NOT NULL DEFAULT 'translate'
        )
        ''')
        try:
            await db.execute("ALTER TABLE sessions ADD COLUMN interview_question_id INTEGER")
        except sqlite3.OperationalError:
            pass  # the column already exists
        try:
            await db.execute("ALTER TABLE sessions ADD COLUMN quiz_answer TEXT")
        except sqlite3.OperationalError:
            pass  # the column already exists

        await db.execute('''
        CREATE TABLE IF NOT EXISTS grammar_attempts (
            attempt_id TEXT PRIMARY KEY,
            user_id INTEGER NOT NULL,
            theme TEXT NOT NULL,
            unit INTEGER,
            question_number INTEGER NOT NULL,
            picked_position INTEGER NOT NULL,
            correct_position INTEGER NOT NULL,
            timestamp INTEGER NOT NULL
        )
        ''')
        await db.execute('CREATE INDEX IF NOT EXISTS grammar_attempts_user ON grammar_attempts (user_id)')
        await db.commit()


async def save_grammar_attempt(attempt_id, user_id, theme, unit, question_number, picked, correct):
    """Record one graded answer; repeated callbacks cannot count it twice."""
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute('''
            INSERT INTO grammar_attempts
                (attempt_id, user_id, theme, unit, question_number,
                 picked_position, correct_position, timestamp)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(attempt_id) DO NOTHING
        ''', (attempt_id, user_id, theme, unit, question_number, picked, correct, int(time.time())))
        await db.commit()


async def get_grammar_stats(user_id):
    """Return (answered, correct) for a Telegram user."""
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute('''
            SELECT COUNT(*), COALESCE(SUM(picked_position = correct_position), 0)
            FROM grammar_attempts WHERE user_id = ?
        ''', (user_id,)) as cursor:
            return await cursor.fetchone()

async def save_message(message_id, chat_id, user_id, message_text, reply_to_message_id=None, session_id=None):
    """Save a sent message to the database."""
    print(f"Saving message {message_id} in chat {chat_id}: {message_text!r}")
    try:
        async with aiosqlite.connect(DB_PATH) as db:
            await db.execute(
                "INSERT INTO messages (message_id, chat_id, user_id, message_text, timestamp, reply_to_message_id, session_id) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (message_id, chat_id, user_id, message_text, int(time.time()), reply_to_message_id, session_id)
            )
            await db.commit()
        print(f"Saved message {message_id} successfully")
    except Exception as e:
        print(f"Error saving message {message_id} in chat {chat_id}: {e}")

async def save_reaction(message_id, user_id, emoji):
    """Save a reaction to the database."""
    try:
        async with aiosqlite.connect(DB_PATH) as db:
            await db.execute(
                "INSERT INTO reactions (message_id, user_id, emoji, timestamp) VALUES (?, ?, ?, ?)",
                (message_id, user_id, emoji, int(time.time()))
            )
            await db.commit()
    except Exception as e:
        print(f"Error saving reaction for message {message_id}: {e}")

async def get_message_by_id(message_id, chat_id):
    """Retrieve a message from the database by its ID and Chat ID."""
    try:
        async with aiosqlite.connect(DB_PATH) as db:
            db.row_factory = aiosqlite.Row
            async with db.execute(
                "SELECT * FROM messages WHERE message_id = ? AND chat_id = ?",
                (message_id, chat_id)
            ) as cursor:
                row = await cursor.fetchone()
                if row:
                    return dict(row)
                return None
    except Exception as e:
        print(f"Error retrieving message {message_id} in chat {chat_id}: {e}")
        return None

async def get_messages_by_session(session_id, limit=None, *, user_id=None):
    """Return session messages in chronological order, optionally filtered by sender."""
    try:
        async with aiosqlite.connect(DB_PATH) as db:
            query = "SELECT message_text FROM messages WHERE session_id = ?"
            args = [session_id]
            if user_id is not None:
                query += " AND user_id = ?"
                args.append(user_id)
            if limit is not None:
                query += " ORDER BY timestamp DESC, rowid DESC LIMIT ?"
                args.append(limit)
            else:
                query += " ORDER BY timestamp, rowid"
            async with db.execute(query, args) as cursor:
                rows = await cursor.fetchall()
                messages = [row[0] for row in rows]
                if limit is not None:
                    messages = list(reversed(messages))
                return messages
    except Exception as e:
        print(f"Error retrieving messages for session {session_id}: {e}")
        return []


async def create_session(user_id):
    """Insert a new session row and return session_id."""
    session_id = str(uuid.uuid4())
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "INSERT INTO sessions (session_id, user_id, created_at, session_state) VALUES (?, ?, ?, ?)",
            (session_id, user_id, int(time.time()), 'translate')
        )
        await db.commit()
    return session_id


async def set_session_state(session_id, state, *, quiz_answer=None):
    """Update the mode and keep a pending translation only in quiz mode."""
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "UPDATE sessions SET session_state = ?, quiz_answer = ? WHERE session_id = ?",
            (state, quiz_answer if state == 'quiz' else None, session_id)
        )
        await db.commit()


async def set_interview_question(session_id, question_id):
    """Store the id of the interview question waiting for an answer (None clears it)."""
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "UPDATE sessions SET interview_question_id = ? WHERE session_id = ?",
            (question_id, session_id)
        )
        await db.commit()


async def get_session(user_id):
    """Return the active session for user_id (within 3600s or with a pending quiz).
    If none exists, create one and return it."""
    now = int(time.time())
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute(
            """SELECT * FROM sessions WHERE user_id = ?
               AND ((? - created_at) < 3600 OR (session_state = 'quiz' AND quiz_answer IS NOT NULL))
               ORDER BY created_at DESC LIMIT 1""",
            (user_id, now)
        ) as cursor:
            row = await cursor.fetchone()
            if row:
                return dict(row)
    session_id = await create_session(user_id)
    return {'session_id': session_id, 'user_id': user_id, 'created_at': now, 'session_state': 'translate'}
