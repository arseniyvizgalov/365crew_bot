from aiogram import Router, F
from aiogram.types import Message, FSInputFile, CallbackQuery
from aiogram.filters import CommandStart
from client_bot.kb import start_kb
from pathlib import Path

PHOTO_PATH = Path(__file__).parent / "start_photo.jpg"
router = Router()
text = "Рады тебя видеть в 365Store!✌️ Мы готовы тебе помочь!⬇️"

@router.message(CommandStart())
async def start(message: Message):
    photo = FSInputFile(PHOTO_PATH)
    await message.answer_photo(photo=photo, caption=text, reply_markup=start_kb)

@router.callback_query(F.data == 'back_start')
async def back(callback: CallbackQuery):
    await callback.answer()
    if callback.message.photo:
        await callback.message.edit_caption(caption=text, reply_markup=start_kb)
    else:
        await callback.message.delete()
        photo = FSInputFile(PHOTO_PATH)
        await callback.message.answer_photo(photo=photo, caption=text, reply_markup=start_kb)

@router.callback_query(F.data == 'back_preorder')
async def back_preorder(callback: CallbackQuery):
    await callback.answer()
    photo = FSInputFile(PHOTO_PATH)
    await callback.message.answer_photo(photo=photo, caption=text, reply_markup=start_kb)


@router.message(F.text == '◀️В главное меню')
async def back_preorder(message: Message):
    photo = FSInputFile(PHOTO_PATH)
    await message.delete()
    await message.answer_photo(photo=photo, caption=text, reply_markup=start_kb)

