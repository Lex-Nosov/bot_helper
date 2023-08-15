from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def main_butt(size=2):
    markup = ReplyKeyboardMarkup(row_width=size, resize_keyboard=True)
    row = ["удалить своего пользователя", "Создать напоминание"]
    markup.add(*row)
    return markup
