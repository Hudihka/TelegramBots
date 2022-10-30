import telebot

bot = telebot.TeleBot('5626067599:AAG2Zs0SfUTcp9RONiI9cS4oj5tW1whQSQ4')


@bot.message_handler(commands=['test'])
def start(message):
    # отправка сообщения в чат
    # можно задать 3тий параметр parse_mode='html' и это говорит о том, что текст
    # можно выводить как html меняя ширифт и цвет например
    bot.send_message(message.chat.id, '<b>Привет</b>', parse_mode='html')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    # reply_to ответить на сообщение
    bot.reply_to(message, "Howdy, how are you doing?")


# бот работает без остановки
bot.polling(none_stop=True)
