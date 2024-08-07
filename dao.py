import asyncio
from enum import Enum
import aiosqlite as asql
import sqlite3 as sql


async def __start() -> None:
    async with asql.connect("users.db") as db:
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


async def register_user(username: str, chat_id: int) -> None:
    async with asql.connect("users.db") as db:
        await db.execute(
            f"""
            INSERT INTO Users
            VALUES ('{username}', {chat_id})
            """
        )
        await db.commit()


async def unregister_user(username: str, chat_id: int) -> None:
    async with asql.connect("users.db") as db:
        await db.execute(
            f"""
            DELETE FROM Users
            WHERE username == '{username}' AND chat_id = {chat_id}
            """
        )
        await db.commit()


async def get_users_from_chat(chat_id: int) -> list[str]:
    async with asql.connect("users.db") as db:
        res = await db.execute(
            f"""
            SELECT username
            FROM Users
            WHERE chat_id = {chat_id}
            """
        )
        return [s for s, in await res.fetchall()]
