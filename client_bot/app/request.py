from aiogram import F, Router
from aiogram.types import CallbackQuery, Message
from client_bot.app.db import MY_REQUESTS
from client_bot.kb import back_start, back_reply_kb

router = Router()


@router.callback_query(F.data == "req")
async def show_requests(callback: CallbackQuery):
    await callback.message.delete()
    await callback.answer()
    items = MY_REQUESTS.get(callback.from_user.id, [])
    if not items:
        return await callback.message.answer("Пока заявок нет", reply_markup=back_start)

    for i, r in enumerate(items, 1):
        cap = (
            f"🧾 <b>Заявка #{i}</b>\n"
            f"<b>Модель:</b> {r['model']}\n"
            f"<b>Размер:</b> {r['size']}\n"
            f"<b>Фото:</b> {'есть' if r['photo'] else 'нет'}"
        )
        if r["photo"]:
            await callback.message.answer_photo(r["photo"], caption=cap, parse_mode="HTML")
        else:
            await callback.message.answer(cap, parse_mode="HTML")
    await callback.message.answer(
        "Это все заявки!",
        reply_markup=back_reply_kb
    )