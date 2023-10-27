import telebot
bot = telebot.TeleBot("token")
first_button = telebot.types.InlineKeyboardButton("Downloader_bot", url="https://t.me/Danlodrbot")
markup = telebot.types.InlineKeyboardMarkup()
markup.add(first_button)
key_button = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
key_button.add("TwiteNudes", "Ssskade", "baad_pussy")
# get_contact = telebot.types.KeyboardButton("black")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'hi\nwelcome', reply_markup=markup)


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, 'what can i do for you baby?', reply_markup=key_button)


@bot.message_handler()
def keyboard_help(message):
    if message.text == "TwiteNudes":
        bot.send_message(message.chat.id, "@TwiteNuds_Bot")
    elif message.text == "Ssskade":
        bot.send_message(message.chat.id, "@Sskkadebot")
    elif message.text == "baad_pussy":
        bot.send_message(message.chat.id, "@baad_pussy_Bot")


bot.infinity_polling()

