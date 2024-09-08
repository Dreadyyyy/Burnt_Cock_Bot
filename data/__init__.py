import aiosqlite as asql
import asyncio


async def __start() -> None:
    async with asql.connect("data/users.db") as db:
        cur = await db.execute(
            """
            SELECT EXISTS 
            (
            SELECT 1 FROM sqlite_master
            WHERE name="Users" AND type ="table"
            )
            """
        )
        if not (await cur.fetchone() or (0,))[0]:
            await db.execute(
                """
                CREATE TABLE Users
                (
                    username TEXT,
                    chat_id INTEGER,
                    unique(username, chat_id)
                )
                """
            )
            await db.commit()


asyncio.run(__start())
