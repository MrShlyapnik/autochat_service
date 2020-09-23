from services.parser import parser
from services.api import api_ls, api_chat
import requests
import openpyxl
table={
    'Казань':   'https://docs.google.com/spreadsheets/d/1EhE-amKJjSLcu5KMZNbIzotWpbAoYF5GbgZ9VIKueKc/export?format=xlsx&id=1EhE-amKJjSLcu5KMZNbIzotWpbAoYF5GbgZ9VIKueKc',
    'Москва':   'https://docs.google.com/spreadsheets/d/1dhTz3mTVYd1y9KqdCd1KUbY0AmyaZhVdOQ6qTX9b9C4/export?format=xlsx&id=1dhTz3mTVYd1y9KqdCd1KUbY0AmyaZhVdOQ6qTX9b9C4',
    }
messages_array=api_ls()
town='Казань'
r = requests.get(table[town])
f = open(town+'.xlsx', 'wb')
f.write(r.content)
f.close()

wb=openpyxl.load_workbook(town+'.xlsx',  data_only=True)
for message in messages_array:
    # print(message)
    for m in messages_array[message]:
        parser(m,message, wb)
messages_array=api_chat()
for message in messages_array:
    # print(message)
    for m in messages_array[message]:
        parser(m,message, wb)