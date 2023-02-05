from aiogram.fsm.state import StatesGroup, State


class MainMenu(StatesGroup):
    greetings = State()
    subscription = State()
    features = State()


class WorkManagement(StatesGroup):
    proposal = State()
    test_category_choice = State()
    knowledge_base_branches = State()
