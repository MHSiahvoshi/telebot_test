import telebot
bot = telebot.TeleBot("6732287229:AAEHcZFArgAgw_XKx8ZJHChzGRcSpZU8apo")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'hi\nwelcome')


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "What can i do for you?")


bot.infinity_polling()

