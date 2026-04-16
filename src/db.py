import time
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

        await db.execute('''
        CREATE TABLE IF NOT EXISTS translations (
            english_message TEXT NOT NULL,
            russian_message TEXT NOT NULL
        )
        ''')
        
        await db.commit()

async def save_message(message_id, chat_id, user_id, message_text, reply_to_message_id=None):
    """Save a sent message to the database."""
    print(f"Saving message {message_id} in chat {chat_id}: {message_text!r}")
    try:
        async with aiosqlite.connect(DB_PATH) as db:
            await db.execute(
                "INSERT INTO messages (message_id, chat_id, user_id, message_text, timestamp, reply_to_message_id) VALUES (?, ?, ?, ?, ?, ?)",
                (message_id, chat_id, user_id, message_text, int(time.time()), reply_to_message_id)
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