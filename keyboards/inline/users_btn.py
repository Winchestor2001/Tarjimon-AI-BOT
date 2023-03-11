from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def languages_btn():
    btn = InlineKeyboardMarkup(row_width=2)
    btn.add(
        InlineKeyboardButton('UZ', callback_data='lang:uz'),
        InlineKeyboardButton('RU', callback_data='lang:ru'),
        InlineKeyboardButton('EN', callback_data='lang:en'),
    )
    return btn







