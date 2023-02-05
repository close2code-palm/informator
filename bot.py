import asyncio

from aiogram import Bot, Dispatcher
from aiogram_dialog import DialogRegistry

from config import read_config
from dialogs import entry_dialog, profile_dialog, contacts
from routers import entry_router


async def main():
    config = read_config('config.ini')
    bot = Bot(token=config.telegram.bot_token)
    disp = Dispatcher()
    registry = DialogRegistry(disp)
    registry.register(entry_dialog.dialog)
    registry.register(profile_dialog.dialog)
    registry.register(contacts.contacts_dialog)
    disp.include_router(entry_router.router)
    disp['chan'] = 'https://t.me/pyoungs'
    await disp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        ...
