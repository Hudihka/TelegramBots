import telebot
import time

bot = telebot.TeleBot('5747667746:AAGM-pY5RnoZSO3rREJB-vW0mrvmntG__Es')


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
name_owner = 'hudihka'


@bot.message_handler(commands=['activate'])
def activate_bot(message):
    nameUser = message.from_user.username
    if nameUser == name_owner:
        message_lol(message)
    else:
        activate_zaeb(message)


def message_lol(message):
    text_bold = 'АХАХАХАХАХА'
    text_usualu = '\nты дымал я тебе разрешу его запускать?'

    bot.reply_to(message, f'<b>{text_bold}</b>{text_usualu}', parse_mode='html')


def activate_zaeb(message):
    ignor = True
    mess_ale_first = 'АЛЕЕЕЕ БЛЯТЬ!!!'
    mess_ale_second = '\nОТВЕТЬ БРАТЮНЕ'
    count = 100

    for i in range(count):
        if not ignor:
            return
        time.sleep(i)
        bot.send_message(message.chat.id, f'<b>{mess_ale_first}</b>{mess_ale_second}', parse_mode='html')


@bot.message_handler()
def lisen(message):
    if ignor && nameUser != name_owner:
        bot.send_message(message.chat.id, f'<b>{mess_ale_first}</b>{mess_ale_second}', parse_mode='html')
        bot.reply_to(message, 'А сразу нельзя было?')



bot.polling(none_stop=True)