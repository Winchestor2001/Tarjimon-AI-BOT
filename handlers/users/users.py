from aiogram import Dispatcher
from aiogram.types import *

from keyboards.inline.users_btn import languages_btn
from loader import dp
from utils.misc.text_translator import text_trans


async def bot_start(message: Message):
    await message.answer(f"Salom")


async def get_user_text_handler(message: Message):
    text = message.text
    btn = await languages_btn()
    await message.answer(text, reply_markup=btn)


async def select_lang_callback(call: CallbackQuery):
    lang = call.data.split(":")[-1]
    context = call.message.text
    result = await text_trans(context, lang)
    btn = await languages_btn()
    await call.message.edit_text(result, reply_markup=btn)


def register_users_py(dp: Dispatcher):
    dp.register_message_handler(bot_start, commands=['start'])
    dp.register_message_handler(get_user_text_handler, content_types=['text'])

    dp.register_callback_query_handler(select_lang_callback, text_contains='lang:')
