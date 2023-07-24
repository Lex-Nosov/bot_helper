from telebot.async_telebot import AsyncTeleBot
import asyncio

from config import API_TOKEN

bot = AsyncTeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
async def welcome_message(message):
    await bot.reply_to(message, 'Hello, Lex')


if __name__ == '__main__':
    asyncio.run(bot.polling())
