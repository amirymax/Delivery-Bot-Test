from aiogram import Router
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import json

from api_token import ADMIN_ID

user_router = Router()
MENU_FILE = "menu.json"


def load_menu():
    try:
        with open(MENU_FILE, "r") as f:
            return json.load(f)
    except json.decoder.JSONDecodeError:
        return []


class OrderState(StatesGroup):
    choosing = State()
    confirming = State()


@user_router.message(Command('start'))
async def start(message: Message):
    await message.answer('Хуш омадед ба боти доставка!\n\nБарои менюро дидан, командаи /menu равон кунед')


@user_router.message(Command('menu'))
async def menu(message: Message, state: FSMContext):
    menu = load_menu()
    if not menu:
        await message.answer('Меню ҳоло холӣ аст...')
        return

    buttons = [
        [InlineKeyboardButton(
            text=f"{item['name']} - {item['price']} сомонӣ", callback_data=item['name'])]
        for item in menu
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=buttons)
    await message.answer('Ин менюи мо аст:', reply_markup=markup)
    await state.set_state(OrderState.choosing)

@user_router.callback_query(OrderState.choosing)
async def choose(callback: CallbackQuery, state: FSMContext):
    await state.update_data(item = callback.data)
    await callback.message.answer(f"Шумо интихоб кардед: {callback.data}. Барои тасдиқ /confirm равон кунед")
    await state.set_state(OrderState.confirming)
    await callback.answer()

@user_router.message(OrderState.confirming)
async def confirm(message: Message, state: FSMContext):
    data = await state.get_data()
    item = data.get('item')
    print('State data:', data)
    if not item:
        await message.answer('Аввал аз меню интихоб кунед')
        return

    await message.answer(f"Фармоиши шумо: {item} тасдиқ шуд. Ташаккур")
    await message.bot.send_message(ADMIN_ID, f"Фармоиши нав: {item} аз {message.from_user.full_name}")
    await state.clear()




