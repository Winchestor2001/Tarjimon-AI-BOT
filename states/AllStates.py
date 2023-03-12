from aiogram.dispatcher.filters.state import StatesGroup, State


class AdminStates(StatesGroup):
    send_message_to_users = State()
