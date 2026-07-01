# Bibliotecas
import aiosqlite
import asyncio
import os


dreamdb = "yume.db"


async def db_init():

    async with aiosqlite.connect(dreamdb) as db:

        await db.execute("I did an oopsie here :c")

        await db.commit()

asyncio.run(db_init())
