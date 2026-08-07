# Bibliotecas
import aiosqlite


dreamdb = "yume.db"


async def db_init():
    async with aiosqlite.connect(dreamdb) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS guild_settings(
                guild_id INTEGER PRIMARY KEY,
                language TEXT DEFAULT 'en',
                personality TEXT DEFAULT 'default' 
            )
        """)
        await db.commit()


async def guild_settings_get(guild_id: int) -> tuple[str, str]:
    async with aiosqlite.connect(dreamdb) as db:
        async with db.execute("SELECT language, personality FROM guild_settings WHERE guild_id = ?", (guild_id,)) as cursor:
            row = await cursor.fetchone()

            return (row[0], row[1]) if row else ('en', 'default')


async def guild_language_set(guild_id: int, language: str):
    async with aiosqlite.connect(dreamdb) as db:
        await db.execute("""
            INSERT INTO guild_settings (guild_id, language)
            VALUES (?, ?)
            ON CONFLICT(guild_id) DO UPDATE SET language = excluded.language
        """, (guild_id, language))
        await db.commit()


async def guild_personality_set(guild_id: int, personality: str):
    async with aiosqlite.connect(dreamdb) as db:
        await db.execute("""
            INSERT INTO guild_settings (guild_id, personality)
            VALUES (?, ?)
            ON CONFLICT(guild_id) DO UPDATE SET personality = excluded.personality
        """, (guild_id, personality))
        await db.commit()