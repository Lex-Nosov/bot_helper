from telebot.async_telebot import AsyncTeleBot
import asyncio

from config import API_TOKEN
from remainder_db_handler import User

bot = AsyncTeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
async def welcome_message(message):
    user = User(message.chat.id, message.from_user.first_name)
    await user.add_user()
    await bot.reply_to(message, f'Hello, {message.from_user.first_name}')


@bot.message_handler(commands=['delete'])
async def delete_user(message):
    user = User(message.chat.id, message.from_user.first_name)
    await user.remove_user()
    await bot.reply_to(message, f'User {message.from_user.first_name} deleted')


@bot.message_handler(commands=['remainder'])
async def remainder(message):
    await bot.send_message(message.chat.id, 'какое событие нужно запомнить?')


if __name__ == '__main__':
    asyncio.run(bot.polling())
