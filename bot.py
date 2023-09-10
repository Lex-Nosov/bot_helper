from telebot.async_telebot import AsyncTeleBot
import asyncio
import os
import re

from config import API_TOKEN
from remainder_db_handler import User, table_creation, Remainder
from buttons import main_butt

bot = AsyncTeleBot(API_TOKEN)


async def table_check():
    path = os.getcwd()
    files = os.listdir(path)
    for name_file in files:
        if re.search('sqlite', name_file):
            return
    await table_creation()


@bot.message_handler(commands=['start'])
async def welcome_message(message):
    user = User(message.chat.id, message.from_user.first_name)
    await user.check_user()
    await bot.reply_to(message, f'Привет, {message.from_user.first_name}! Добро пожаловать в бота-помощника :)')
    await bot.send_message(message.from_user.id, 'Выбери действие', reply_markup=main_butt())


@bot.message_handler(commands=['delete'])
async def delete_user(message):
    user = User(message.chat.id, message.from_user.first_name)
    await user.remove_user()
    await bot.reply_to(message, f'User {message.from_user.first_name} deleted')


@bot.message_handler(commands=['remainder'])
async def remainder(message):
    await bot.send_message(message.chat.id, 'Введите через символ обратный слеш "/" "Тема / Описание')


# @bot.message_handler(func=lambda message: message.text == re.search("/", message.text))
# def create_remainder(message):
#     data = message.text.split('/')
#     subject = data[0]
#     description = data[1]
#     remainder = Remainder(subject, description, message.from_user.id)
#     remainder.add_remainder()


if __name__ == '__main__':
    asyncio.run(table_check())
    asyncio.run(bot.polling())
