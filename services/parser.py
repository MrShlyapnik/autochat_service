from .table import table
import openpyxl
import requests
import telebot

from .info import INFO
from .info1 import INFO1

token = '1155265832:AAEkQP-ces-BicmhsIZVRk9HW3Envsg6n0Q'
bot = telebot.TeleBot(token)
def parser(message, phone, wb):
    print('Parser {}'.format(phone))
    text = message
    months = [
        'январь',
        'февраль',
        'март',
        'апрель',
        'май',
        'июнь',
        'июль',
        'август',
        'сентябрь',
        'октябрь',
        'ноябрь',
        'декабрь',
    ]
    message = text.lower()
    for month in months:
        message = message.replace(month, ' ' + month + ' ')
    message = message.replace("-", " ")
    message = message.replace("Занятые даты", " ")
    message = message.replace("Занятые даты!", " ")
    message = message.replace("занятые даты!", " ")
    message = message.replace("!", " ")
    message = message.replace(";", " ")
    message = message.replace(".", "")
    message = message.replace("🏡", ' ')
    message = message.replace("✅", ' ')
    message = message.replace("⛔", ' ')
    message = message.replace("🧸", ' ')
    message = message.replace("🔥", ' ')
    message = message.replace("🌅", ' ')
    message = message.replace("🏘", ' ')
    message = message.replace("\n", " ")
    message = message.replace(":", " ")
    message = message.replace(",", " ")
    message = message.replace("(", " ")
    message = message.replace(")", " ")
    message = message.replace("     ", " ")
    message = message.replace("    ", " ")
    message = message.replace("   ", " ")
    message = message.replace("  ", " ")
    message = message.replace("*", " ")
    new_formating_message = ""
    info = INFO
    info1 = INFO1
    for i in info1:
        message = message.replace(i, i.replace(" ", ""))
    message = message.replace("     ", " ")
    message = message.replace("    ", " ")
    message = message.replace("   ", " ")
    message = message.replace("  ", " ")
    house = ""
    month = ""
    if len(info[phone]) == 1:
        for h in info[phone]:
            house = h

    if phone == '79600323247' or phone == '79178670299':
        for word in message.split(" "):
            if word not in info[phone]:
                if word.lower() not in months:
                    if word.isdigit():
                        if int(word) <= 0 or int(word) >= 32:
                            continue
                    else:
                        continue
                else:
                    month = word.lower()
                    continue
            if word in info[phone]:
                house = word
                continue
            else:
                if house != "":
                    if (word.lower() in months):

                        try:
                            print(len(info[phone][house][month]))
                        except BaseException:
                            info[phone][house][month] = []
                            house = ""

                    else:
                        try:
                            try:
                                info[phone][house][month].append(word)
                            except BaseException:
                                info[phone][house][month] = []
                                info[phone][house][month].append(word)
                        except BaseException:
                            print("Error")
    else:
        
        for word in message.split(" "):
            if phone in '79655888066-1485072828@g.us':
                for h in info[phone]:
                    if h in word:
                        word = h
                        break
            
            if word not in info[phone]:
                if word.lower() not in months:
                    if word.isdigit():
                        if int(word) <= 0 or int(word) >= 32:
                            continue
                    else:
                        continue
                else:
                    month = word.lower()
            
            if word in info[phone]:
                house = word
            else:
                if house != "":
                    if (word.lower() in months):
                        try:
                            print(len(info[phone][house][month]))
                        except BaseException:
                            info[phone][house][month] = []

                    else:
                        try:
                            info[phone][house][month].append(word)
                        except BaseException:
                            pass
    # print(info[phone])

    bot.send_message(381666837, str(info[phone]))
    table(info, phone, wb)