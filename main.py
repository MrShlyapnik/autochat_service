from services.parser import parser
from services.api import api_ls, api_chat
import requests
import datetime
import openpyxl
table={
    'Казань':   'https://docs.google.com/spreadsheets/d/1JIstqYbaPS6ZkzbH7AmZ0xeb7VbMpmA6GrhPiZ5r5iY/export?format=xlsx&id=1JIstqYbaPS6ZkzbH7AmZ0xeb7VbMpmA6GrhPiZ5r5iY',
    'Москва':   'https://docs.google.com/spreadsheets/d/1dhTz3mTVYd1y9KqdCd1KUbY0AmyaZhVdOQ6qTX9b9C4/export?format=xlsx&id=1dhTz3mTVYd1y9KqdCd1KUbY0AmyaZhVdOQ6qTX9b9C4',
    }
# messages_array=api_ls()

f=open('time.txt','r')
last=f.read()
f.close()
print(last)
last=last.replace('\n', '')
last=datetime.datetime.strptime(last, '%Y-%m-%d %H:%M:%S')
print("Check date")
if (datetime.datetime.now()-last).total_seconds()>=1800:
    print("Start main")
    town='Казань'
    r = requests.get(table[town])
    print('Load')
    f = open(town+'.xlsx', 'wb')
    f.write(r.content)
    f.close()

    wb=openpyxl.load_workbook(town+'.xlsx',  data_only=True)
    messages_array=api_ls()
    print('Load')

    for message in messages_array:
        # print(message)
        try:
            for m in messages_array[message]:
                parser(m,message, wb)
        except:
            print('error')
    messages_array=api_chat()
    print('Load')
    print(len(messages_array))
    for message in messages_array:
        print(messages_array[message])
        try:
            for m in messages_array[message]:
                print("Parser")
                parser(m,message, wb)
        except:
            print('error')

    r = requests.get(table[town])
    f = open('../katalog_bot/Vtripe/'+town+'_date.xlsx', 'wb')
    f.write(r.content)
    f.close()
    f=open('time.txt','w')
    f.write(str(datetime.datetime.now()).split('.')[0])
    f.close()
    print('End')
