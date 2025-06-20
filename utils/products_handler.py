from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

#my imports
from .db_utils import Categories
from .states import CategoryState, ProductState

router3 = Router()

@router3.message(Command('list_categories'))
async def list_categories(message:Message):
    await message.answer(Categories.list_categories())

@router3.message(Command('add_category'))
async def add_category_handler(message:Message, state: FSMContext):
    await message.answer('Kategoriya ismini kiriting')
    await state.clear()
    await state.set_state(CategoryState.name)

@router3.message(CategoryState.name)
async def add_category(message:Message, state:FSMContext):
    if Categories.add_category(message.text):await message.answer('Successfully added');return
    await message.answer('It already exist or internal server error')