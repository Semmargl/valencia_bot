import config
import telebot

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли
    if message.text == "Cкажы секрет":
        bot.send_message(message.chat.id, "Серега душка")
    else:
        bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
     bot.infinity_polling()