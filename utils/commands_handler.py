from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram.types import Message

# my imports
from .states import RegisterState
from .db_utils import Users

router1 = Router()

@router1.message(Command('start'))
async def start_handler(message:Message) -> None:
    if Users.is_registered(message.from_user.id):await message.reply('Qaytganingizdan Xursandmiz!');return # type: ignore
    await message.answer("Hush kelibsiz botga")

@router1.message(Command('register'))
async def get_first_name(message:Message, state:FSMContext) -> None:
    if Users.is_registered(message.from_user.id):await message.reply('Siz oldin registratsiyadan o\'tgansiz!');return # type: ignore
    try:
        await state.clear()
        await state.update_data(id=message.from_user.id) # type: ignore
        await message.answer('Registratsiya jarayonini boshlaymiz\n'
                             'Iltimos ismingizni kiriting')
        await state.set_state(RegisterState.first_name)
    except Exception as e:print(e)