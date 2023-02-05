from typing import Any

from aiogram import types
from aiogram_dialog import Dialog, Window, DialogManager, Data
from aiogram_dialog.widgets.kbd import Button, Row, Cancel
from aiogram_dialog.widgets.text import Const, Format

from states.profile import ProfileData, Contacts


async def get_profile(dialog_manager: DialogManager, **kwargs):
    return {'age': 33, 'sex': 'M', 'spec': 'Pythonista',
            'full_name': 'Julian',
            'contact': dialog_manager.dialog_data.get(
                'contact', 'julyfortune101@gmail.com')}


async def fill_age(call: types.CallbackQuery, but: Button,
                   dialog_manager: DialogManager):
    await dialog_manager.switch_to(ProfileData.age)


async def set_spec(call: types.CallbackQuery, but: Button,
                   dialog_manager: DialogManager):
    await dialog_manager.switch_to(ProfileData.specialization)


async def fname(call: types.CallbackQuery, but: Button,
                dialog_manager: DialogManager):
    await dialog_manager.switch_to(ProfileData.full_name)


async def set_sex(call: types.CallbackQuery, but: Button,
                  dialog_manager: DialogManager):
    await dialog_manager.switch_to(ProfileData.sex)


async def set_contacts(call: types.CallbackQuery, but: Button,
                       dialog_manager: DialogManager):
    await dialog_manager.start(Contacts.contacts)


async def process_result(start_data: Data, result: Any,
                         manager: DialogManager):
    if 'contact' in result:
        manager.dialog_data['contact'] = result['contact']


dialog = Dialog(
    Window(
        Const('Your profile looks like this now'),
        Row(Button(Format('Age -> {age}'), id='fill_age',
                   on_click=fill_age),
            Button(Format('Sex -> {sex}'), id='set_sex',
                   on_click=set_sex)),
        Button(Format('Your specialization -> {spec}'),
               id='set_spec', on_click=set_spec),
        Button(Format('Full name -> {full_name}'), id='full_name',
               on_click=fname),
        Button(Format('Contacts -> {contact}'), id='contact',
               on_click=set_contacts),
        Cancel(),
        state=ProfileData.profile_view,
        getter=get_profile,
    ),
    on_process_result=process_result
)
