from aiogram import executor

from handlers.users.users import register_users_py
from loader import dp
import middlewares, filters, handlers
from utils.set_bot_commands import set_default_commands
from handlers.admins.admins import register_admins_py


async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)

    register_admins_py(dispatcher)
    register_users_py(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)

