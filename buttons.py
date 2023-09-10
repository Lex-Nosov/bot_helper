from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup


def main_butt():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    button_create_remainder = KeyboardButton('создать напоминание')
    markup.add(button_create_remainder)
    return markup
