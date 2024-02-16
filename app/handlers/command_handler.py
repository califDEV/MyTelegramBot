import telebot


from telebot.util import generate_random_token
from app.keyboards import inline

admin = ['6815312419']

class Commands:
    def __init__(self, bot):
        self.bot = bot

        @bot.message_handler(commands=["start"])
        def send_welcome(message):
            bot.send_message(message.chat.id, "<b>Привет, я телеграм бот написанный @californidze\n\n"
                "Этого бота я делал для своего развития в сфере разработке ботов)\n"
                "И с каждым днем я буду развивать и улучшать этот проект и доведу его до идеала</b>", reply_markup=inline.start)

        @bot.message_handler(commands=["help"])
        def help_command(message):
            bot.send_message(message.chat.id, f"<b>Привет! вот весь список моих команд:\n\n"
                    "Основные комманды:\n"
                    "/start -> запускает бота так-же открывает меню\n/help -> Открывает списко всех комманд бота\n"
                    "/menu -> Открывает меню. Так-же можно открыть меню написав \"Меню\"\n"
                    "/contact -> Даст все контакты для связи со мною\n\nДоп.Команды:\n"
                    "/profile -> Откроет ваш профишь\n/balance ->Если вы хотите посмотреть свой баланс, но не хотите открывать профиль\n"
                    "/shop -> тут будут все мои услуги. Закаать так же можно через бота, или написав мне в лс</b>")
        
        @bot.message_handler(commands=["menu"])
        def menu_command(message):
            bot.send_message(message.chat.id, f"<b>Вот твое меню:</b>\n\n",reply_markup=inline.menu)
        
        @bot.message_handler(commands=["admin"])
        def admin_panel(message):
            if str(message.from_user.id) not in admin:
                bot.send_message(message.chat.id, "sᴏʀʏ ʏᴏᴜ ɴᴏᴛ ᴀᴅᴍɪɴ", reply_to_message_id=message.message_id)
            else:
                bot.send_message(message.chat.id, f"ᴀɴᴅʀᴇʏ, ᴡᴇʟʟᴄᴏᴍᴇ ᴛᴏ ᴀᴅᴍɪɴ ᴘᴀɴᴇʟ", reply_to_message_id=message.message_id)
        
        @bot.message_handler(func=lambda message: True)
        def echo_message(message):
            bot.reply_to(message, "<b>Извините но я не ИИ. Я не могу отвечать на обычные сообщение</b>\n\n"
                "/start -> откроет меню бота\n/help -> Откроет список всех команд бота")