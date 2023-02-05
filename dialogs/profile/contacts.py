from aiogram.types import CallbackQuery, Message
from aiogram_dialog import Window, Dialog, DialogManager
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button, Cancel
from aiogram_dialog.widgets.text import Const, Format

from states.profile import Contacts


async def get_contacts(dialog_manager: DialogManager, **kwargs):
    return {'phone': '+79789205317',
            'email': 'julyfortune101@gmail.com',
            'socials': dialog_manager.dialog_data.get(
                'socials', 'Telegram ot counts!')}


async def save_contacts(callback: CallbackQuery, button: Button,
                        manager: DialogManager):
    for k in 'phone', 'email', 'social':
        if k in manager.dialog_data:
            valueable_contact = manager.dialog_data[k]
            break
        else:
            valueable_contact = 'Just here'
    await manager.done(result={'contact': valueable_contact})


async def handle_email(message: Message, message_input: MessageInput,
                       manager: DialogManager):
    manager.dialog_data['email'] = message.text
    await manager.switch_to(Contacts.contacts)


async def handle_social(message: Message, message_input: MessageInput,
                        manager: DialogManager):
    manager.dialog_data['social'] = message.text
    await manager.switch_to(Contacts.contacts)


async def handle_phone(message: Message, message_input: MessageInput,
                       manager: DialogManager):
    manager.dialog_data['phone'] = message.text
    await manager.switch_to(Contacts.contacts)


async def set_email(call: CallbackQuery, button: Button,
                    manager: DialogManager):
    await manager.switch_to(Contacts.email)


async def set_phone(call: CallbackQuery, button: Button,
                    manager: DialogManager):
    await manager.switch_to(Contacts.phone)


async def set_social(call: CallbackQuery, button: Button,
                     manager: DialogManager):
    await manager.switch_to(Contacts.social_media)


contacts_dialog = Dialog(
    Window(
        Const('Here you can leave information'
              ' and then we can communicate with you'),
        Button(Format('Email -> {email}'), id='email',
               on_click=set_email),
        Button(Format('Phone number -> {phone}'),
               id='phone', on_click=set_phone),
        Button(Format('Social networks -> {socials}'),
               id='socials', on_click=set_social),
        Button(Format('Save and up'), id='save_contacts',
               on_click=save_contacts),
        Cancel(),
        state=Contacts.contacts, getter=get_contacts
    ),
    Window(
        Const('Enter your email'),
        MessageInput(handle_email),
        state=Contacts.email
    ),
    Window(Const('Enter your phone'),
           MessageInput(handle_phone),
           state=Contacts.phone),
    Window(Const('Enter your favourite media'),
           MessageInput(handle_social),
           state=Contacts.social_media)
)
