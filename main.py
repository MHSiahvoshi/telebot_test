import telebot
bot = telebot.TeleBot("6732287229:AAEHcZFArgAgw_XKx8ZJHChzGRcSpZU8apo")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'hi\nwelcome')


bot.infinity_polling()

