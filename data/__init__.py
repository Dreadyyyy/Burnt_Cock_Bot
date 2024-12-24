import aiosqlite as asql
import asyncio


async def __start() -> None:
    async with asql.connect("data/users.db") as db:
        await db.execute(
            """
            CREATE TABLE IF NOT EXISTS Users
            (
                username TEXT NOT NULL,
                chat_id INTEGER NOT NULL,
                UNIQUE(username, chat_id)
            )
            """
        )
        await db.commit()


asyncio.run(__start())
