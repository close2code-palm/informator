from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram_dialog import DialogManager

from states.base_states import MainMenu

router = Router()


@router.message(CommandStart)
async def handle_start(m: types.Message, dialog_manager: DialogManager):
    await dialog_manager.start(state=MainMenu.greetings, data={
        'user': m.from_user.username,
    })
