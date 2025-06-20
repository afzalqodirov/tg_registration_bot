from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

#my imports
from .db_utils import Categories, Products
from .states import CategoryState, ProductState

router3 = Router()

@router3.message(Command('list_categories'))
async def list_categories(message:Message):
    await message.answer(Categories.list_categories())

@router3.message(Command('add_category'))
async def add_category_handler(message:Message, state: FSMContext):
    print('The add category is working?')
    await message.answer('Kategoriya ismini kiriting')
    await state.clear()
    await state.set_state(CategoryState.name)

@router3.message(CategoryState.name)
async def add_category(message:Message, state:FSMContext):
    if Categories.add_category(message.text):await message.answer('Successfully added');return
    await message.answer('It already exist or internal server error')

@router3.message(Command('list_products'))
async def list_products(message:Message):
    await message.answer(Products.list_products())

@router3.message(Command('add_product'))
async def add_product(message:Message, state:FSMContext):
    await message.answer('Product nomini kiriting')
    await state.clear()
    await state.set_state(ProductState.name)

@router3.message(ProductState.name)
async def product_name(message:Message, state:FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(ProductState.category)
    await message.answer("Endi kategoriya nomini kiriting")

@router3.message(ProductState.category)
async def product_category(message:Message, state:FSMContext):
    try:await state.update_data(category=message.text)
    except Exception as e:print(e)
    await state.set_state(ProductState.description)
    await message.answer('Description yozing')

@router3.message(ProductState.description)
async def product_description(message:Message, state:FSMContext):
    await state.update_data(description=message.text)
    data = await state.get_data()
    if Products.add_product(**data):await message.answer("Successfully added")
    else:await message.answer("A problem occured while adding a product")

@router3.message(Command('search_category'))
async def search_category(message:Message, state:FSMContext):
    await state.clear()
    await state.set_state(CategoryState.search)
    await message.answer('Search uchun parameter yozing')

@router3.message(CategoryState.search)
async def search_with_query(message:Message, state:FSMContext):
    await message.answer(Categories.list_categories(message.text))