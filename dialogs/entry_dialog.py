from aiogram_dialog import Dialog, Window, DialogManager
from aiogram_dialog.widgets.kbd import Column, Next, Url, Back, Start
from aiogram_dialog.widgets.text import Const, Format

from states.base_states import MainMenu
from states.profile import ProfileData


async def get_data(dialog_manager: DialogManager, chan, **kwargs):
    return {
        "chan": chan,
        "user": dialog_manager.start_data.get("user") or "Friend",
    }

# When user is unknown - welcome, else some statistics
dialog = Dialog(
    Window(
        Const('Welcome to <b>Gocio</b> TaaS!'
              'Here you can test, exploit and '
              'report legal targets for free'),
        Column(
            Start(Const('Fill profile'), id='fill_profile',
                  state=ProfileData.profile_view),
            Next(text=Const('Features')),
            Url(Format('Subscribe, dear {user}!'), Format('{chan}'))
        ),
        getter=get_data,
        parse_mode="HTML",
        state=MainMenu.greetings
    ),
    Window(
        Const('You will:'),
        Const('Have easy interface for trivial testing operations'),
        Const('Get access to well mapped resources which will help you a lot'),
        Back(),
        state=MainMenu.features
    )
)
