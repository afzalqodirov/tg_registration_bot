from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

#my imports
from .states import RegisterState
from .db_utils import Users
from config import phone_markup

router2 = Router()

@router2.message(RegisterState.first_name)
async def register_first_name(message:Message, state:FSMContext):
    await state.update_data(first_name=message.text)
    await state.set_state(RegisterState.last_name)
    await message.answer('Endi familiyangizni kiriting')

@router2.message(RegisterState.last_name)
async def register_last_name(message:Message, state:FSMContext):
    await state.update_data(last_name=message.text)
    await state.set_state(RegisterState.phone_number)
    await message.answer('Iltimos telefon raqamingizni yuboring', reply_markup=phone_markup)
    
@router2.message(RegisterState.phone_number, F.contact)
async def register_phone_number(message:Message, state:FSMContext):
    await state.update_data(phone_number=message.contact.phone_number) # type: ignore
    data = await state.get_data()
    if Users.add_user(**data):await message.answer('Siz muvaffaqiyatli registratsiyadan o\'tdingiz!')
    else:await message.answer('An error occured while registering you')

@router2.message(RegisterState.phone_number)
async def register_phone_number_error(message:Message, state:FSMContext):
    await message.answer('Iltimos telefon raqamingizni kiritmang!\n'
    'Telefon raqamingizni <b>yuboring!</b>', reply_markup=phone_markup, parse_mode="HTML")
    await state.set_state(RegisterState.phone_number)