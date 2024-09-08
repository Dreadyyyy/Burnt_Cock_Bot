import asyncio
import logging

from telegram import start

logging.basicConfig(level=logging.INFO)


async def main() -> None:
    await start()


if __name__ == "__main__":
    asyncio.run(main())
