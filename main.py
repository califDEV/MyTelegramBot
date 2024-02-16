import telebot
import logging
import os

from app.handlers.command_handler import Commands
from app.callbacks.start_callback import StartCallbacks
from app.callbacks.menu_callback import MenuCallbacks
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(token, parse_mode="HTML")

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

# Подключаем к main.py

commands_instance = Commands(bot)
start_callbacks_instance = StartCallbacks(bot)
menu_callbacks_instance = MenuCallbacks(bot)

bot.infinity_polling(allowed_updates=True)