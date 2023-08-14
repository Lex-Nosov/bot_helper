from telebot.async_telebot import AsyncTeleBot
import asyncio

from config import API_TOKEN
from remainder_db_handler import add_user

bot = AsyncTeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
async def welcome_message(message):
    await add_user(message.chat.id, message.from_user.first_name)
    await bot.reply_to(message, f'Hello, {message.from_user.first_name}')


@bot.message_handler(commands=['remainder'])
async def remainder(message):
    await bot.send_message(message.chat.id, 'какое событие нужно запомнить?')


if __name__ == '__main__':
    asyncio.run(bot.polling())
