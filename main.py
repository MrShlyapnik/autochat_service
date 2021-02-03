from services.parser import parser
from services.api import api_ls, api_chat
import requests
import datetime
import openpyxl
table = {
    'Казань': 'https://docs.google.com/spreadsheets/d/1JIstqYbaPS6ZkzbH7AmZ0xeb7VbMpmA6GrhPiZ5r5iY/export?format=xlsx&id=1JIstqYbaPS6ZkzbH7AmZ0xeb7VbMpmA6GrhPiZ5r5iY',
    'Москва': 'https://docs.google.com/spreadsheets/d/1dhTz3mTVYd1y9KqdCd1KUbY0AmyaZhVdOQ6qTX9b9C4/export?format=xlsx&id=1dhTz3mTVYd1y9KqdCd1KUbY0AmyaZhVdOQ6qTX9b9C4',
}
town = 'Казань'

f = open('time.txt', 'r')
last_update = f.read()
f.close()

last_update = last_update.replace('\n', '')

last_update = datetime.datetime.strptime(last_update, '%Y-%m-%d %H:%M:%S')

if (datetime.datetime.now() - last_update).total_seconds() >= 900:

    r = requests.get(table[town])
    f = open(town + '.xlsx', 'wb')
    f.write(r.content)
    f.close()

    wb = openpyxl.load_workbook(town + '.xlsx', data_only=True)

    messages_list = api_ls()

    for message in messages_list:
        for m in messages_list[message]:
            if m is not None:
                parser(m, message, wb)
    messages_list = api_chat()
    for message in messages_list:
        for m in messages_list[message]:
            if m is not None:
                parser(m, message, wb)

    r = requests.get(table[town])
    f = open('../katalog_bot/Vtripe/' + town + '_date.xlsx', 'wb')
    f.write(r.content)
    f.close()
    f = open('time.txt', 'w')
    f.write(str(datetime.datetime.now()).split('.')[0])
    f.close()
