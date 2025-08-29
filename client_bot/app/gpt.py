from aiogram import F, Router
from aiogram.types import CallbackQuery, Message, FSInputFile, ReplyKeyboardRemove
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from openai import AsyncOpenAI
import os
from dotenv import load_dotenv
from client_bot.kb import back_gpt, start_kb
from pathlib import Path

load_dotenv()
PHOTO_PATH = Path(__file__).parent / "start_photo.jpg"
router = Router()
client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = (
    "Ты дружелюбный консультант 365Store. Отвечай только по делу. Доставка только по израилю, товар только оригинальный. Если не можешь ответтить, говори: свяжитесь с @sxvkaaa "
)
MODEL = "gpt-4o-mini"

class ChatStates(StatesGroup):
    consultant = State()

@router.callback_query(F.data == "gpt")
async def consultant_on(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await state.set_state(ChatStates.consultant)
    await callback.message.answer(
        "Консультант включён ✅ Напиши свой вопрос:",
        reply_markup=back_gpt
    )

@router.message(F.text == "◀️Назад", ChatStates.consultant)
async def consultant_off(message: Message, state: FSMContext):
    await state.clear()
    await message.answer('Надеюсь я смог помочь!', reply_markup=ReplyKeyboardRemove())
    text = "Рады тебя видеть в 365Store!✌️ Мы готовы тебе помочь!⬇️"
    await message.delete()
    photo = FSInputFile(PHOTO_PATH)
    await message.answer_photo(photo=photo, caption=text, reply_markup=start_kb)


@router.message(ChatStates.consultant)
async def consultant_answer(message: Message, state: FSMContext):
    user_text = message.text.strip()

    data = await state.get_data()
    history = data.get("history", [])

    history.append({"role": "user", "content": user_text})

    resp = await client.responses.create(
        model=MODEL,
        input=[{"role": "system", "content": SYSTEM_PROMPT}] + history,
    )

    answer_text = resp.output_text or "Извини, не смог придумать ответ 🙈"

    history.append({"role": "assistant", "content": answer_text})
    await state.update_data(history=history)

    await message.answer(answer_text)