from aiogram.dispatcher.filters.state import State, StatesGroup


class UserState(StatesGroup):
    schedule_for = State()
    schedule_name = State()
    schedule_desc = State()
    schedule_deadline = State()
    schedule_delete = State()
    scheduel_change = State()
    scheduel_change_for_whom = State()
    scheduel_change_name = State()
    scheduel_change_descrip = State()
    scheduel_change_deadline = State()
