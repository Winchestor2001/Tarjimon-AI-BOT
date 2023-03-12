from aiogram.dispatcher import FSMContext
from aiogram.utils.exceptions import BotBlocked

from loader import bot
from aiogram.types import Message, CallbackQuery
from data.config import ADMINS
from aiogram import Dispatcher
from keyboards.inline.admins_btn import admin_btn
from keyboards.default.admins_btn import cancel_btn, remove
from database.connections import count_users, get_users_id
from states.AllStates import AdminStates
import asyncio


async def start_admin_handler(message: Message):
    user_id = message.from_user.id
    if user_id in ADMINS:
        btn = await admin_btn()
        users = await count_users()
        await message.answer(f"Siz admin paneldasiz:\n\n"
                             f"Bot azolar soni: {users} ta", reply_markup=btn)


async def send_message_to_users_callback(call: CallbackQuery):
    await call.message.delete()
    btn = await cancel_btn()
    await call.message.answer("Xabaringizni yo`llang...", reply_markup=btn)
    await AdminStates.send_message_to_users.set()


async def get_admin_message_state(message: Message, state: FSMContext):
    content = message.content_type
    btn = message.reply_markup
    users = await get_users_id()
    try:
        context = message.html_text
    except:
        context = None

    sent = 0
    no_sent = 0

    if content == 'text' and message.text == '❌ Bekor qilish':
        await message.answer("❌ Bekor qilindi", reply_markup=remove)
        await start_admin_handler(message)
        await state.finish()
        return

    await message.answer("Xabar yo`llash boshlandi", reply_markup=remove)
    await state.finish()

    for user in users:

        try:
            if content == 'text':
                await bot.send_message(user['user_id'], context, reply_markup=btn)

            elif content == 'photo':
                await bot.send_photo(user['user_id'], photo=message.photo[-1].file_id, caption=context,
                                     reply_markup=btn)

            elif content == 'video':
                await bot.send_video(user['user_id'], video=message.video.file_id, caption=context,
                                     reply_markup=btn)

            elif content == 'document':
                await bot.send_document(user['user_id'], document=message.document.file_id, caption=context,
                                        reply_markup=btn)

            elif content == 'audio':
                await bot.send_audio(user['user_id'], audio=message.audio.file_id, caption=context,
                                     reply_markup=btn)

            elif content == 'animation':
                await bot.send_animation(user['user_id'], animation=message.animation.file_id,
                                         caption=context, reply_markup=btn)

            await asyncio.sleep(0.3)
            sent += 1

        except BotBlocked:
            no_sent += 1
            continue

    await message.answer(f"Yuborildi: {sent}\n"
                         f"Etibormadi: {no_sent}")


def register_admins_py(dp: Dispatcher):
    dp.register_message_handler(start_admin_handler, commands=['admin'])
    dp.register_message_handler(get_admin_message_state, state=AdminStates.send_message_to_users,
                                content_types=['text', 'document', 'video', 'audio', 'photo', 'animation'])

    dp.register_callback_query_handler(send_message_to_users_callback, text='send')
