import telebot
from telebot import types
import time

bot = telebot.TeleBot('5747667746:AAGM-pY5RnoZSO3rREJB-vW0mrvmntG__Es')


ignor_value: bool = False
COUNT = 100
NAME_OWNER = 'hudihka'

bot.set_my_commands([
    telebot.types.BotCommand("start", "включаем режим заебы")
])


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
    if ignor_value:
        return
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
