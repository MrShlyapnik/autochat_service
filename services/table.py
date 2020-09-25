import os
import requests
import time
import openpyxl
import json
import gspread
import datetime
import sys
import httplib2
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient import discovery


def table(info,phone, wb):
    full_name={
        '79053116753':
    {
        'домбогородское': '*Вилла Богородское*',
            'домшапши': '*Высокая гора (шапшы)*',
    },
    '79063257387':
    {
        'малый': '*Голубое озеро №2 малый*',
            'большой': '*Голубое озеро №3*',
    },
    '79600363975':
    {
         'зеленыйминдаль': '*Голубое озеро №6*',
       'салмачи': '*Салмачи №1 Жк Вознесенье*',
    },
    '79377771034':
    {
        'деревянный': '*Дербышки №1 дер*',
            'кирпичный': '*Дербышки №2 кир*',
    },
    '79047619866':
    {
        'замок': '*Кадышего №1 VIP*',
            'сруб': '*Кадышего №2 дерево*',
            'дворец': '*Кадышего №3 дворец*',
    },
    '79656012318':
    {
        'бавария': '*Константиновка №1 Бавария*',
        'константиновка':'*Константиновка №3 хансувар*',
        'панорама':'*Конастантиновка №2 у озера*',
    },
    '79872974084':
    {
        'амалый': '*Самосырова 5 малый*',
            'бсредний': '*Самосырова 6 средний*',
            'вбольшой': '*Самосырова 7 большой*',
    },
    '79274226911':
    {
        'чайка1': '*Щербаково 1 (Чайка)*',
            'чайка2': '*Щербаково 2*',
    },
    '79050212617':
    {
        'дом': '*Кульсеитово 1 ВИП*',
        'русская': '*Кульсеитово 2 Русский*',
        'охотничья': '*Кульсеитово 3 Охотничий*',
        'берег': '*Кульсеитово №7 Турецкий*	берег',
        'парк': '*Кульсеитово №8*',
    },
    '79872971476-1481554579@g.us':
    {
        'к1': '*Константиновка #6*',
            'к3': '*Константиновка #7*',
            'к4': '*контантиновка #8*',
    },
    '79178767741-1419363809@g.us':
    {
        'банкетныйзал': '*Казанка Банкетный зал*',
            '1рыцарский': '*Новкая сосновка. Рыцар*',
            '2vip': '*Новая сосновка.Вип*',
            '3классический': '*Новая сосновка. Классич*',
            '4восточный1': '*Новая сосновка Восточный 1*',
            '5восточный2': '*Новая сосновка Восточный 2*',
            '6японский': '*Новая сосновка Японский*',
            '7гостевой': '*Новая сосновка Гостевой*',
            '8казанка':'*Казанка*',

    },
    '79655807679-1585037693@g.us':
    {
        'царский': '*Кадышево №4 голубое царский 50 чел*',
            'сосновый': '*Кадышево №5 голубое сосновый 30 чел*',
            'панорама': '*Кадышево №6 Беседка 80 чел*',
            'апартаменты': '*Кадышево №7 Аппартаменты*',
            'дятлово':'*Дятлово комплекс*',
    },
    '79655888066-1485072828@g.us':
    {
       'малый': '*Салмачи №2 Малый*',
            'большой': '*Салмачи №3 Японский*',
            '3новый': '*Салмачи №4 Новый*',
    },
    '79655896555-1527783737@g.us':
    {
        'малый':'*Самосырова 2*',
            'большой':'*Самосырова 3 Большой*',
    },
    
        #    'домброгородское': '*Вилла богородское*',
        #     'домшапши': '*Высокая гора (шапшы)*',
        #     'дятлово': '*Дятлово комплекс*',
        #     'набережная3': '*Горнолыжка 1*',
        #     'нагоре/141': '*Горнолыжка 2*',
        #     'набережная4': '*Горнолыжка 3*',
        #     'малый': '*Голубое озеро №2 малый*',
        #     'большой': '*Голубое озеро №3*',
        #     'зеленыйминдаль': '*Голубое озеро №6*',
        #     'деревянный': '*Дербышки №1 дер*',
        #     'кирпичный': '*Дербышки №2 кир*',
        #     'замок': '*Кадышего №1 VIP*',
        #     'сруб': '*Кадышего №2 дерево*',
        #     'дворец': '*Кадышего №3 дворец*',
        #     'царский': '*Кадышево №4 голубое царский 50 чел*',
        #     'сосновый': '*Кадышево №5 голубое сосновый 30 чел*',
        #     'панорама': '*Кадышево №6 Беседка 80 чел*',
        #     'апартаменты': '*Кадышево №7 Аппартаменты*',
        #     'бавария': '*Константиновка №1 Бавария*',
        #     'контсантиновка': '*Конастантиновка №2 у озера*',
        #     'к1': '*Константиновка №3 хансувар*',
        #     'к3': '*Константиновка #6*',
        #     'к4': '*Константиновка #7*',
        #     'дом': '*контантиновка #8*',
        #     'русская': '*Кульсеитово 1 ВИП*',
        #     'охотничья': '*Кульсеитово 2 Русский*',
        #     'берег': '*Кульсеитово 3 Охотничий*',
        #     'парк': '*Кульсеитово №7 Турецкий*',
        #     'кощаково': '*Кульсеитово №8*',
        #     'занято': '*Кощаково VIP*',
        #     '8казанка': '*Кощаково Premium*',
        #     'банкетныйзал': '*Казанка*',
        #     '1рыцарский': '*Казанка Банкетный зал*',
        #     '2vip': '*Новкая сосновка. Рыцар*',
        #     '3классический': '*Новая сосновка.Вип*',
        #     '4восточный1': '*Новая сосновка. Классич*',
        #     '5восточный2': '*Новая сосновка Восточный 1*',
        #     '6японский': '*Новая сосновка Восточный 2*',
        #     '7гостевой': '*Новая сосновка Японский*',
        #     'а': '*Новая сосновка Гостевой*',
        #     'б': '*Нагорный Сруб1*',
        #     'в': '*Нагорный сруб2*',
        #     'г': '*Нагорный сруб3*',
        #     'салмачи': '*Нагорный сруб4*',
        #     'новый': '*Салмачи №1 Жк Вознесенье*',
        #     'мал': '*Салмачи №2 Малый*',
        #     'малбас': '*Салмачи №3 Японский*',
        #     'сред': '*Салмачи №4 Новый*',
        #     'больш': '*Салмачи №7 Деревянный*',
        #     'амалый': '*Салмачи №8 Деревянный с бассейном*',
        #     'бсредний': '*Салмачи №9 VIP средний*',
        #     'вбольшой': '*Салмачи №10 VIP большой с бассейном*',
        #     'чайка1': '*Салмачи №12  Премиум*',
        #     'чайка2': '*Самосырова 2*',
    }
    table={
    'Казань':   'https://docs.google.com/spreadsheets/d/1JIstqYbaPS6ZkzbH7AmZ0xeb7VbMpmA6GrhPiZ5r5iY/export?format=xlsx&id=1JIstqYbaPS6ZkzbH7AmZ0xeb7VbMpmA6GrhPiZ5r5iY',
    'Москва':   'https://docs.google.com/spreadsheets/d/1dhTz3mTVYd1y9KqdCd1KUbY0AmyaZhVdOQ6qTX9b9C4/export?format=xlsx&id=1dhTz3mTVYd1y9KqdCd1KUbY0AmyaZhVdOQ6qTX9b9C4',
    }
    #получаем доступ к гугл таблице
    json_key = json.load(open('creds.json'))  # json credentials you downloaded earlier
    scope = ['https://spreadsheets.google.com/feeds',
                'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scopes=scope)
    httpAuth = credentials.authorize(httplib2.Http())
    service = discovery.build('sheets', 'v4', http = httpAuth)

    file = gspread.authorize(credentials)  # authenticate with Google
    sheet = file.open_by_url("https://docs.google.com/spreadsheets/d/1JIstqYbaPS6ZkzbH7AmZ0xeb7VbMpmA6GrhPiZ5r5iY/edit#gid=955783345")

    # town='Казань'
    # r = requests.get(table[town])
    # f = open(town+'.xlsx', 'wb')
    # f.write(r.content)
    # f.close()

    # wb=openpyxl.load_workbook(town+'.xlsx',  data_only=True)
    date_list=wb["даты"]
    sheet=sheet.get_worksheet(5)
    month_code={
        'январь':1,
        'февраль':2,
        'март':3,
        'апрель':4,
        'май':5,
        'июнь':6,
        'июль':7,
        'август':8,
        'сентябрь':9,
        'октябрь':10,
        'ноябрь':11,
        'декабрь':12,
    }
    year=0
    m=0
    day=0
    for house in info[phone]:
        if house=='8казанка':
            continue
        print(house)
        stop=True
        if(len(info[phone][house])!=0):
            for month in info[phone][house]:
               
                if len(info[phone][house][month])!=0:
                    m=month_code[month]
                    if month_code[month]<datetime.datetime.now().month:
                        year=datetime.datetime.now().year+1
                    else:
                        year=datetime.datetime.now().year
                    last_day=0
                    for d in info[phone][house][month]:
                        if last_day!=0 and int(d)<last_day:
                            break
                        last_day=int(d)
                        day=int(d)
                        date=datetime.date(year, m, day)
                        if date<datetime.datetime.now().date():
                            continue
                        scip=0
                        col=30
                        stop=True
                        date_list=wb["даты"]
                        for row in date_list.rows:
                            if scip==0:
                                scip+=1
                                continue
                            # print(str(row[col].value).split(' ')[0])
                            # print(str(date))
                            
                            while stop==True:
                                # print(d
                                # ate)
                                # print(str(row[col].value).split(' ')[0])
                                # print(date)
                                if str(row[col].value).split(' ')[0]==str(date):
                                    # print('1')
                                    row_number=-1
                                    for r in date_list.rows:
                                        row_number+=1
                                        # print("2")
                                        # print(r[441].value)
                                        # print(house)
                                        if str(r[27].value)==full_name[phone][house]:
                                            DATA = {'requests': [{'repeatCell':
                                                    {'range': 
                                                        { 
                                                            "sheetId":955783345,
                                                        'startRowIndex': row_number, # номер строки (нумерация с 0) с которой включительно будет применено форматирование
                                                        'endRowIndex': row_number+1, # номер строки до которой будет применено форматирование, не включительно
                                                            
                                                        'startColumnIndex': col, # номер столбца (нумерация с 0)…
                                                        'endColumnIndex': col+1
                                                        },
                                                    
                                                    'cell':  {'userEnteredFormat': {'backgroundColor': {'red': 0,
                                                                                                        'green':0,
                                                                                                        'blue':128,
                                                    }}},

                                                    'fields': 'userEnteredFormat', # другие параметры форматирования ячейки будут сброшены
                                                }}
                                                ]}
                                            if r[col].fill.fgColor.rgb=="FF38761D" or r[col].fill.fgColor.rgb=="FF93C47D":
                                                stop=False
                                                break
                                            service.spreadsheets().batchUpdate(spreadsheetId = '1JIstqYbaPS6ZkzbH7AmZ0xeb7VbMpmA6GrhPiZ5r5iY', body=DATA).execute()
                                            print('3')
                                            time.sleep(5)
                                            stop=False
                                            break

                                col+=1
                            break

