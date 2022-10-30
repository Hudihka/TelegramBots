import telebot
import time

bot = telebot.TeleBot('5747667746:AAGM-pY5RnoZSO3rREJB-vW0mrvmntG__Es')


ignor: bool = False
COUNT = 100
NAME_OWNER = 'hudihka00'


@bot.message_handler(commands=['activate'])
def activate_bot(message):
    nameUser = message.from_user.username
    if nameUser == NAME_OWNER:
        message_lol(message)
    else:
        activate_zaeb(message)


def message_lol(message):
    text_bold = 'АХАХАХАХАХА'
    text_normal = '\nты думал я тебе разрешу его запускать?'

    bot.reply_to(message, f'<b>{text_bold}</b>{text_normal}', parse_mode='html')


def activate_zaeb(message):
    ignor = True
    mess_ale_first = 'АЛЕЕЕЕEEE БЛЯТЬ!!!'
    mess_ale_second = '\nОТВЕТЬ БРАТЮНЕ'

    for i in range(COUNT):
        if not ignor:
            return
        time.sleep(i)
        bot.send_message(message.chat.id, f'<b>{mess_ale_first}</b>{mess_ale_second}', parse_mode='html')


@bot.message_handler()
def lissen(message):
    nameUser = message.from_user.username
    if nameUser != NAME_OWNER:
        # ignor = False
        photo = open('IMG_0160.JPG', 'rb')
        bot.send_photo(photo)
        bot.reply_to(message, 'А сразу нельзя было?')


bot.polling(none_stop=True)
