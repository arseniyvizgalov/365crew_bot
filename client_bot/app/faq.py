from aiogram import F, Router
from aiogram.types import CallbackQuery, FSInputFile
from client_bot.kb import faq_kb, back_faq
from pathlib import Path

router = Router()
GROKIT_PATH = Path(__file__).parent / "grokit.jpg"
PHOTO_PATH = Path(__file__).parent / "start_photo.jpg"

@router.callback_query(F.data == "faq")
async def faq(callback: CallbackQuery):
        await callback.answer()
        await callback.message.edit_caption(caption="Ответы на ваши вопросы!", reply_markup=faq_kb)


@router.callback_query(F.data == "back_faq")
async def faq(callback: CallbackQuery):
        await callback.answer()
        await callback.message.delete()
        photo = FSInputFile(PHOTO_PATH)
        await callback.message.answer_photo(photo=photo, caption="Ответы на ваши вопросы!", reply_markup=faq_kb)


@router.callback_query(F.data == "order_faq")
async def order_faq(callback: CallbackQuery):
    await callback.answer()
    await callback.message.delete()
    await callback.message.answer("*Ответ по заказу*", reply_markup=back_faq)

@router.callback_query(F.data == "legit_faq")
async def legit_faq(callback: CallbackQuery):
    await callback.answer()
    await callback.message.delete()
    await callback.message.answer("*Ответ по легитимности*", reply_markup=back_faq)

@router.callback_query(F.data == "delivery_faq")
async def delivery_faq(callback: CallbackQuery):
    await callback.answer()
    await callback.message.delete()
    await callback.message.answer("*Ответ по доставке*", reply_markup=back_faq)

@router.callback_query(F.data == "grokit_faq")
async def grokit_faq(callback: CallbackQuery):
    await callback.answer()
    await callback.message.delete()
    photo = FSInputFile(GROKIT_PATH)
    await callback.message.answer_photo(photo=photo, caption="*Ответ про Grokit*", reply_markup=back_faq)




