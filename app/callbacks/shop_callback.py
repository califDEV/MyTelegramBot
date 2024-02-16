from telebot import TeleBot
from app.keyboards import inline

class ShopCallbacks:
    def __init__(self, bot):
        self.bot = bot
        
        @bot.callback_query_handler(func=lambda call: call.data == 'pay_bot')
        def pay_bot_callback(call):
            # Ваш код для обработки callback_data 'open_menu'
            self.bot.send_message(call.message.chat.id, "<b>Если вы хотите заказать"
                                " Телеграм бота то вам стоит написать мне, или узнать цены в тгк</b>",reply_markup=inline.contacts)