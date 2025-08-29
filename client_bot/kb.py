from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

start_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Заказать вещи', callback_data='order')],
    [InlineKeyboardButton(text='FAQ', callback_data='faq')],
    [InlineKeyboardButton(text='Консультант(24/7)', callback_data='gpt')],
    [InlineKeyboardButton(text='Заявки', callback_data='req')],
])

faq_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Как сделать заказ?', callback_data='order_faq')],
    [InlineKeyboardButton(text='Легит или нет?', callback_data='legit_faq')],
    [InlineKeyboardButton(text='Как происходит доставка?', callback_data='delivery_faq')],
    [InlineKeyboardButton(text='Кто создал бота?', callback_data='grokit_faq')],
    [InlineKeyboardButton(text='◀️Назад', callback_data='back_start')],
])

back_faq = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='◀️Назад', callback_data='back_faq')],
])

back_start = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='◀️Назад', callback_data='back_start')],
])

back_gpt = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="◀️Назад")]],
    resize_keyboard=True
)

order_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Из наличия', callback_data='order_db'),
     InlineKeyboardButton(text='Под заказ', callback_data='preorder')],
    [InlineKeyboardButton(text='◀️Назад', callback_data='back_start')],
])

back_order = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="⏪Назад")]
    ],
    resize_keyboard=True
)

ready_kb = ReplyKeyboardMarkup(
    keyboard=[
    [KeyboardButton(text='Поехали')],
    [KeyboardButton(text='Назад')],
],
    resize_keyboard=True
)

no_photo_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Нет фото')],
    ]
)

preorder_done_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='В меню', callback_data='back_preorder')],
])

back_reply_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='◀️В главное меню')],
])



