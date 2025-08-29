from aiogram import F, Router
from aiogram.types import CallbackQuery, Message, ReplyKeyboardRemove, FSInputFile
from client_bot.kb import order_kb, back_order
from pathlib import Path

PHOTO_PATH = Path(__file__).parent / "start_photo.jpg"
router = Router()

@router.callback_query(F.data == 'order')
async def order(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_caption(caption='Заказать одежду из 365Store можно двумя способами!\n\n1.Заказать товар из наличия\n2.Оставить заявку на товар под заказ\n\nВыберите нужный вариант⬇️', reply_markup=order_kb)

@router.callback_query(F.data == "order_db")
async def order_db(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(
        "Введите id товара:",
        reply_markup=back_order
    )

@router.message(F.text == "⏪Назад")
async def order(message: Message):
    await message.delete()
    photo = FSInputFile(PHOTO_PATH)
    await message.answer('🔙', reply_markup=ReplyKeyboardRemove())
    await message.answer_photo(photo=photo, caption='Заказать одежду из 365Store можно двумя способами!\n\n1.Заказать товар из наличия\n2.Оставить заявку на товар под заказ\n\nВыберите нужный вариант⬇️', reply_markup=order_kb)