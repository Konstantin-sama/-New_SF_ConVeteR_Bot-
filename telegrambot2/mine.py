# автор: Калинкин Константин Владимирович
# количество запросов на конвертацию ограничено
# имя телеграмбота: New_SF_Converter # bot in telegram - https://t.me/New_SF_ConVeteR_Bot
import telebot

from config import *

from extensions import Converter, APIException

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    text = 'Приветствие!'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for i in exchanges.keys():
        text = '\n'.join((text, i))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def converter(message: telebot.types.Message):
    try:
        base, sym, amount = message.text.split()
    except ValueError as e:
        bot.reply_to('Неверное количество параметров!')

    try:
        new_price = Converter.get_price(base, sym, amount)
        bot.reply_to(message, f'Цена {amount} {base} в {sym} : {new_price}')

    except APIException as e:
        bot.reply_to(message, f'Ошибка в команде:\n{e}')



bot.polling()