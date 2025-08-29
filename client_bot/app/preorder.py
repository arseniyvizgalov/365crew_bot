from aiogram import F, Router
from aiogram.types import CallbackQuery, Message, ReplyKeyboardRemove, FSInputFile, ContentType
from client_bot.kb import ready_kb, order_kb, no_photo_kb, preorder_done_kb
from pathlib import Path
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from client_bot.app.db import MY_REQUESTS

PHOTO_PATH = Path(__file__).parent / "start_photo.jpg"
router = Router()
class OrderStates(StatesGroup):
    model = State()
    photo = State()
    size = State()




@router.callback_query(F.data == 'preorder')
async def preorder(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer('Мы сформируем заявку и отправим её администратору\nГотовы заполнить заявку?', reply_markup=ready_kb)

@router.message(F.text == "Назад")
async def order(message: Message):
    await message.delete()
    photo = FSInputFile(PHOTO_PATH)
    await message.answer('🔙', reply_markup=ReplyKeyboardRemove())
    await message.answer_photo(photo=photo, caption='Заказать одежду из 365Store можно двумя способами!\n\n1.Заказать товар из наличия\n2.Оставить заявку на товар под заказ\n\nВыберите нужный вариант⬇️', reply_markup=order_kb)

@router.message(F.text == "Поехали")
async def start_order(message: Message, state: FSMContext):
    await state.set_state(OrderStates.model)
    await message.answer(
        "1/3 Введи модель кроссовок (например: Nike Air Max 270):",
        reply_markup=ReplyKeyboardRemove()
    )

@router.message(OrderStates.model, F.text)
async def got_model(message: Message, state: FSMContext):
    model = (message.text or "").strip()
    if len(model) < 2:
        return await message.answer("Слишком коротко. Укажи модель полностью 🙂")
    await state.update_data(model=model)
    await state.set_state(OrderStates.photo)
    await message.answer(
        "2/3️⃣ Пришли фото (как изображение). Если фото нет — нажми «нет фото».",
        reply_markup=no_photo_kb
    )

@router.message(OrderStates.photo, F.content_type == ContentType.PHOTO)
async def got_photo(message: Message, state: FSMContext):
    file_id = message.photo[-1].file_id
    await state.update_data(photo=file_id)
    await state.set_state(OrderStates.size)
    await message.answer(
        "3/3️⃣ Укажи размер (EUR, например: 42):",
        reply_markup=ReplyKeyboardRemove()
    )

@router.message(OrderStates.photo, F.text == 'Нет фото')
async def no_photo(message: Message, state: FSMContext):
    await state.update_data(photo=None)
    await state.set_state(OrderStates.size)
    await message.answer(
        "3/3️⃣ Укажи размер (EUR, например: 42):",
        reply_markup=ReplyKeyboardRemove()
    )

@router.message(OrderStates.size, F.text)
async def got_size(message: Message, state: FSMContext):
    size = (message.text or "").strip()

    data = await state.get_data()
    req = {"model": data["model"], "photo": data.get("photo"), "size": size}

    MY_REQUESTS[message.from_user.id].append(req)

    await state.clear()

    caption = (
        "✅ Заявка создана и добавлена в <b>Мои заявки</b>.\n\n"
        f"<b>Модель:</b> {req['model']}\n"
        f"<b>Размер:</b> {req['size']}\n"
        f"<b>Фото:</b> {'есть' if req['photo'] else 'нет'}"
    )
    if req["photo"]:
        await message.answer_photo(req["photo"], caption=caption, parse_mode="HTML", reply_markup=preorder_done_kb)
    else:
        await message.answer(caption, parse_mode="HTML", reply_markup=preorder_done_kb)




