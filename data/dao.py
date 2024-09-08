from collections.abc import Generator
import aiosqlite as asql


async def register_user(username: str, chat_id: int) -> None:
    async with asql.connect("data/users.db") as db:
        await db.execute(
            f"""
            INSERT INTO Users
            VALUES ('{username}', {chat_id})
            """
        )
        await db.commit()


async def unregister_user(username: str, chat_id: int) -> None:
    async with asql.connect("data/users.db") as db:
        await db.execute(
            f"""
            DELETE FROM Users
            WHERE username = '{username}' AND chat_id = {chat_id}
            """
        )
        await db.commit()


async def get_users_from_chat(chat_id: int) -> Generator[str, None, None]:
    async with asql.connect("data/users.db") as db:
        res = await db.execute(
            f"""
            SELECT username
            FROM Users
            WHERE chat_id = {chat_id}
            """
        )
        return (s for s, in await res.fetchall())
