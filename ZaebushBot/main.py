import telebot
from telebot import types
import time

bot = telebot.TeleBot('5747667746:AAGM-pY5RnoZSO3rREJB-vW0mrvmntG__Es')

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



ignor_value: bool = False
COUNT = 12
NAME_OWNER = 'hudihka'
# COUNT = 70
# NAME_OWNER = 'hudihka'


@bot.message_handler(commands=['start'])
def activate_bot(message):
    nameUser = message.from_user.username
    if nameUser == NAME_OWNER:
        activate_zaeb(message)
    else:
        message_lol(message)


def message_lol(message):
    text_bold = 'АХАХАХАХАХА'
    text_normal = '\nты думал я тебе разрешу его запускать?'

    bot.reply_to(message, f'<b>{text_bold}</b>{text_normal}', parse_mode='html')


def activate_zaeb(message):
    global ignor_value
    ignor_value = True
    mess_ale_first = 'АЛЕЕЕЕEEE БЛЯТЬ!!!'
    mess_ale_second = '\nОТВЕТЬ БРАТЮНЕ'

    for i in range(COUNT):
        if not ignor_value:
            return
        time.sleep(i)
        bot.send_message(message.chat.id, f'<b>{mess_ale_first}</b>{mess_ale_second}', parse_mode='html')


@bot.message_handler()
def messages_listen(message):
    global ignor_value
    nameUser = message.from_user.username
    if nameUser != NAME_OWNER and ignor_value:
        ignor_value = False
        bot.reply_to(message, 'А сразу нельзя было?')
        photo = open('IMG_0160.JPG', 'rb')
        bot.send_photo(message.chat.id, photo)


bot.polling(none_stop=True)