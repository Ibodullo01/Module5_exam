from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def menu_btn():

    k1 = KeyboardButton(text = 'Filial 📍')
    k2 = KeyboardButton(text = 'Start ✅')
    k3 = KeyboardButton(text = '🔙 back')
    k4 = KeyboardButton(text = 'News')
    design = [
        [k1 , k2],
        [k3],
        [k4]
    ]
    return ReplyKeyboardMarkup(keyboard=design , resize_keyboard=True)




