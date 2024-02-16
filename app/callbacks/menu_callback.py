import telebot
from telebot import TeleBot
from app.keyboards import inline
from telebot.util import generate_random_token

class MenuCallbacks:
    def __init__(self, bot):
        self.bot = bot
        
        @bot.callback_query_handler(func=lambda call: call.data == 'open_utils')
        def open_utils_callback(call):
            self.bot.send_message(call.message.chat.id,
                                "<b>Вы перешли в \"ᴜᴛɪʟs🎲\" </b>", reply_markup=inline.utils)
            
            #open_projects
        @bot.callback_query_handler(func=lambda call: call.data == 'open_projects')
        def open_projects_callback(call):
            self.bot.send_message(call.message.chat.id,
                                "<b>Вы перешли в \"ᴍʏ ᴘʀᴏᴊᴇᴄᴛs📁\" </b>", reply_markup=inline.my_projects)
            
        #shop 
        @bot.callback_query_handler(func=lambda call: call.data == 'open_shop')
        def open_shop_callback(call):
            self.bot.send_message(call.message.chat.id,
                                "<b>Вы перешли в \"sʜᴏᴘ🛒\" </b>", reply_markup=inline.shop)
        
        @bot.callback_query_handler(func=lambda call: call.data == 'generate_password')
        def generate_password_callback(call):
            self.bot.send_message(call.message.chat.id, 
                                "<b>Вот твой sᴇᴄʀᴇᴛ ᴘᴀssᴡᴏʀᴅ: "
                                f" <code>{telebot.util.generate_random_token()}</code></b>")
            
        @bot.callback_query_handler(func=lambda call: call.data == 'id_user')
        def id_user_callback(call):
            self.bot.send_message(call.message.chat.id,
                                f"<b>@{call.from_user.username}, ваш  ɪᴅ: <code>{call.from_user.id}</code> </b>")
