from telebot.util import quick_markup


start = quick_markup({
    'ᴍᴇɴᴜ💻': {'callback_data': 'open_menu'},
    'ᴄᴏɴᴛᴀᴄᴛs🔔': {'callback_data': 'send_contacts'},
}, row_width=2)

contacts = quick_markup({
    'ᴄᴀʟɪғᴏʀɴɪᴀ😺': {'url': 'https://t.me/californidze'},
    'ᴄʜᴀɴɴᴇʟ📱': {'url': 'https://t.me/califdev'}
},row_width=2)


menu = quick_markup({
    'sʜᴏᴘ🛒': {'callback_data': 'open_shop'},
    'ᴍʏ ᴘʀᴏᴊᴇᴄᴛs📁': {'callback_data': 'open_projects'},
    'ғᴜɴɴʏ😂': {'callback_data': 'open_funny'},
    'ᴜᴛɪʟs🎲': {'callback_data': 'open_utils'} 
},row_width=2)

utils = quick_markup({
    'ɢᴇɴᴇʀᴀᴛᴇ🔧': {'callback_data': 'generate_password'},
    'ᴍʏ ɪᴅ✨': {'callback_data': 'id_user'}
})


admin_panel = quick_markup({
    'sᴏᴏɴ': {'callback_data': 'soon'}
})