from aiogram.fsm.state import State, StatesGroup

class RegisterState(StatesGroup):
    first_name = State()
    last_name = State()
    phone_number = State()

class ProductState(StatesGroup):
    name = State()
    category = State()
    description = State()

class CategoryState(StatesGroup):
    name = State()
    search = State()