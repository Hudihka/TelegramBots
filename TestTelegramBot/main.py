import telebot
import types from telebot
import time

bot = telebot.TeleBot('5626067599:AAG2Zs0SfUTcp9RONiI9cS4oj5tW1whQSQ4')

addres = 'cd /Users/konstantinirosnikov/Library/Developer/Xcode/Archives/2022-11-01'

# MARK: - Кнопки
# кнопка в сообщени


@bot.message_handler(commands=['test'])
def test(message):
    murkup = types.InlineKeyboardMarkup()
    murkup.add(types.InlineKeyboardButton("посетить сайт", url="https://google.com"))
    bot.send_message(message.chat.id, "Перейти на сайт", reply_markup=murkup)

# кнопки после ввода команды
@bot.message_handler(commands=['test2'])
def test2(message):
    murkup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    website = types.KeyboardButton('web site')
    start = types.KeyboardButton('start')

    murkup.add(website, start)
    bot.send_message(message.chat.id, "Перейти на сайт", reply_markup=murkup)


@bot.message_handler(commands=['test'])
def start(message):
    # отправка сообщения в чат
    # можно задать 3тий параметр parse_mode='html' и это говорит о том, что текст
    # можно выводить как html меняя ширифт и цвет например
    bot.send_message(message.chat.id, '<b>Привет</b>', parse_mode='html')


@bot.message_handler(commands=['name'])
def name(message):
    # отправка имени юзера
    nameUser = message.from_user.username
    bot.send_message(message.chat.id, f'Привет @{nameUser}')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    # reply_to ответить на сообщение
    bot.reply_to(message, "Howdy, how are you doing?")


ignor = False


@bot.message_handler(commands=['ale'])
def ale(message):
    mess_ale_first = 'АЛЕЕЕЕ БЛЯТЬ!!!'
    mess_ale_second = '\nОТВЕТЬ БРАТЮНЕ'
    count = 100

    for i in range(count):
        time.sleep(i)
        bot.send_message(message.chat.id, f'<b>{mess_ale_first}</b>{mess_ale_second}', parse_mode='html')


@bot.message_handler()
def new_message(message):
    mess_ale_first = 'АЛЕЕЕЕ БЛЯТЬ!!!'
    mess_ale_second = '\nОТВЕТЬ БРАТЮНЕ'
    count = 100

    for i in range(count):
        time.sleep(i)
        bot.send_message(message.chat.id, f'<b>{mess_ale_first}</b>{mess_ale_second}', parse_mode='html')


# бот работает без остановки
bot.polling(none_stop=True)
