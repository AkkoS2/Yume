# Bibliotecas
import aiosqlite
import asyncio
import os


dreamdb = "yume.db"


# Just testing stuff

async def db_init():

    async with aiosqlite.connect(dreamdb) as db:

        await db.execute("""

            CREATE TABLE IF NOT EXISTS guild_data (
                         
                         guild_id INTEGER PRIMARY KEY,
                         language TEXT DEFAULT 'en'
                         )
        """)

        await db.commit()

asyncio.run(db_init())
