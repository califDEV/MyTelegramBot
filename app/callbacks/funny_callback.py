from app.keyboards import inline


class FannyCallbacks:
    def __init__(self, bot):
        self.bot = bot
        
        
        @bot.callback_query_handler(func=lambda call: call.data == 'open_funny')
        def pay_bot_callback(call):
            # Ваш код для обработки callback_data 'open_menu'
            self.bot.send_message(call.message.chat.id,"<b>Простите но я ещё ничего не придумал для \"ғᴜɴɴʏ😂\"</b> ")