from aiogram import Bot, Dispatcher
import asyncio
import os
from app import start, faq, request, order, preorder, gpt
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv

load_dotenv()

token = os.environ.get("TELEGRAM_BOT_TOKEN")

bot = Bot(token=token)
dp = Dispatcher(storage=MemoryStorage())


async def main():
    dp.include_router(start.router)
    dp.include_router(faq.router)
    dp.include_router(request.router)
    dp.include_router(order.router)
    dp.include_router(preorder.router)
    dp.include_router(gpt.router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
