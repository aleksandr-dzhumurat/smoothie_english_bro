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
        
        await db.commit()

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


async def get_messages_by_session(session_id, limit=None):
    """Return list of message_text strings for the given session_id, latest first if limit is set."""
    try:
        async with aiosqlite.connect(DB_PATH) as db:
            if limit is not None:
                query = "SELECT message_text FROM messages WHERE session_id = ? ORDER BY timestamp DESC LIMIT ?"
                args = (session_id, limit)
            else:
                query = "SELECT message_text FROM messages WHERE session_id = ? ORDER BY timestamp"
                args = (session_id,)
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


async def set_session_state(session_id, state):
    """Update the session_state for the given session_id."""
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "UPDATE sessions SET session_state = ? WHERE session_id = ?",
            (state, session_id)
        )
        await db.commit()


async def get_session(user_id):
    """Return the active session for user_id (created within last 3600s).
    If none exists, create one and return it."""
    now = int(time.time())
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute(
            "SELECT * FROM sessions WHERE user_id = ? AND (? - created_at) < 3600 ORDER BY created_at DESC LIMIT 1",
            (user_id, now)
        ) as cursor:
            row = await cursor.fetchone()
            if row:
                return dict(row)
    session_id = await create_session(user_id)
    return {'session_id': session_id, 'user_id': user_id, 'created_at': now, 'session_state': 'translate'}