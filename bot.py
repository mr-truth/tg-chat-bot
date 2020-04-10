import telebot
import config

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Ты запустил меня")


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == "привет":
        bot.send_message(message.chat.id, 'Приветствую, создатель')
    elif message.text.lower() == "пока":
        bot.send_message(message.chat.id, 'До встречи, создатель ')
    elif message.text.lower() == "ты хороший":
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAM2XpDFbud8OngAAWQ68Ixrw-FnlSn6AAIwAgAC3PKrB8F0pV76mzL9GAQ')


@bot.message_handler(content_types=['sticker'])
def send_sticker(message):
    print(message)


bot.polling()