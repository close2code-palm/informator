from aiogram.fsm.state import StatesGroup, State


class ProfileData(StatesGroup):
    profile_view = State()
    specialization = State()
    sex = State()
    age = State()
    address = State()
    full_name = State()


class Contacts(StatesGroup):
    contacts = State()

    phone = State()
    social_media = State()
    email = State()
