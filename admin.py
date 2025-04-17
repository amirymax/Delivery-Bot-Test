from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
import json

from api_token import ADMIN_ID


admin_router = Router()

MENU_FILE = "menu.json"

def load_menu():
    try:
        with open(MENU_FILE, "r") as f:
            return json.load(f)
    except json.decoder.JSONDecodeError:
        return []

def save_menu(menu: list):
    with open(MENU_FILE, "w") as f:
        json.dump(menu, f, indent=2)

@admin_router.message(Command('ilova'))
async def ilova(message: Message):
    if message.from_user.id != ADMIN_ID:
        return

    parts = message.text.split(" ", 2)
    if len(parts) < 3:
        await message.answer("Истифода: /ilova <ном> <нарх>")
        return

    name = parts[1]
    price = parts[2]
    menu = load_menu()
    menu.append({"name": name, "price": price})
    save_menu(menu)

    await message.answer(f"Илова шуд: {name} - {price} сомонӣ")

@admin_router.message(Command("gum"))
async def gum(message: Message):
    if message.from_user.id != ADMIN_ID:
        return

    name = message.text.split(" ", 1)[1]
    menu = load_menu()
    menu = [item for item in menu if item['name'] != name]

    save_menu(menu)
    await message.answer(f'Хӯроки {name} гум карда шуд.')
