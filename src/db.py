import time
import aiosqlite


DB_PATH = "bot_messages.db"

async def setup_database():
    """Initialize the database with necessary tables."""
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            message_id INTEGER PRIMARY KEY,
            chat_id INTEGER NOT NULL,
            user_id INTEGER NOT NULL,
            message_text TEXT NOT NULL,
            timestamp INTEGER NOT NULL
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

        await db.execute('''
        CREATE TABLE IF NOT EXISTS translations (
            english_message TEXT NOT NULL,
            russian_message TEXT NOT NULL
        )
        ''')
        
        await db.commit()

async def save_message(message_id, chat_id, user_id, message_text):
    """Save a sent message to the database."""
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "INSERT INTO messages (message_id, chat_id, user_id, message_text, timestamp) VALUES (?, ?, ?, ?, ?)",
            (message_id, chat_id, user_id, message_text, int(time.time()))
        )
        await db.commit()

async def save_reaction(message_id, user_id, emoji):
    """Save a reaction to the database."""
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "INSERT INTO reactions (message_id, user_id, emoji, timestamp) VALUES (?, ?, ?, ?)",
            (message_id, user_id, emoji, int(time.time()))
        )
        await db.commit()

async def get_message_by_id(message_id):
    """Retrieve a message from the database by its ID."""
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute(
            "SELECT * FROM messages WHERE message_id = ?", 
            (message_id,)
        ) as cursor:
            row = await cursor.fetchone()
            if row:
                return dict(row)
            return None