import telebot
from telebot import TeleBot
from app.keyboards import inline
from telebot.util import generate_random_token

class MenuCallbacks:
    def __init__(self, bot):
        self.bot = bot
        
        @bot.callback_query_handler(func=lambda call: call.data == 'open_utils')
        def open_menu_callback(call):
            self.bot.send_message(call.message.chat.id,
                                "<b>Вы перешли в \"ᴜᴛɪʟs🎲\" </b>", reply_markup=inline.utils)
        
        @bot.callback_query_handler(func=lambda call: call.data == 'generate_password')
        def open_menu_callback(call):
            self.bot.send_message(call.message.chat.id, 
                                "<b>Привет! вот твой случайный пароль. Советую его никому не давать"
                                f" <code>{telebot.util.generate_random_token()}</code></b>")
            
        @bot.callback_query_handler(func=lambda call: call.data == 'id_user')
        def soon_callback(call):
            self.bot.send_message(call.message.chat.id,
                                f"<b>@{call.from_user.username},Ваше  ɪᴅ: <code>{call.from_user.id}</code> </b>")
