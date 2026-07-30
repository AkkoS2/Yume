# Bibliotecas
import aiosqlite
import asyncio
import os


dreamdb = "yume.db"


async def db_init():

    async with aiosqlite.connect(dreamdb) as db:
        await db.execute("""

            CREATE TABLE IF NOT EXISTS guild_settings(

                guild_id INTEGER PRIMARY KEY,
                language TEXT DEFAULT 'en'

            )
        """)

        await db.commit()

async def guild_language_get(guild_id: int) -> str:
    async with aiosqlite.connect(dreamdb) as db:
        async with db.execute("SELECT language FROM guild_settings WHERE guild_id = ?", (guild_id)) as cursor:

            row = await cursor.fetchone()
            return row[0] if row else 'en'


async def guild_language_set(guild_id: int, language: str = 'en'):
    async with aiosqlite.connect(dreamdb) as db:
        await db.execute("""

            INSERT INTO guild_settings (guild_id, language)
            VALUES (?, ?)
            ON CONFLICT(guild_id) DO UPDATE SET language = excluded.language

        """, (guild_id, language))

        await db.commit()


asyncio.run(db_init())
