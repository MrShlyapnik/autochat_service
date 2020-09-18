import os
import requests
import time
import openpyxl
import json
import gspread
import datetime
import sys
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient import discovery

def table(info):
    table={
    'Казань':   'https://docs.google.com/spreadsheets/d/1kaAMjkOSWiS3DeUi4J7sKuZy8ow9eht5re_7Ydsg_ZU/export?format=xlsx&id=1kaAMjkOSWiS3DeUi4J7sKuZy8ow9eht5re_7Ydsg_ZU',
    'Москва':   'https://docs.google.com/spreadsheets/d/1dhTz3mTVYd1y9KqdCd1KUbY0AmyaZhVdOQ6qTX9b9C4/export?format=xlsx&id=1dhTz3mTVYd1y9KqdCd1KUbY0AmyaZhVdOQ6qTX9b9C4',
    }
    #получаем доступ к гугл таблице
    json_key = json.load(open('creds.json'))  # json credentials you downloaded earlier
    scope = ['https://spreadsheets.google.com/feeds',
                'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scopes=scope)
    httpAuth = credentials.authorize(httplib2.Http())
    service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)

    file = gspread.authorize(credentials)  # authenticate with Google
    sheet = file.open_by_url("https://docs.google.com/spreadsheets/d/1EhE-amKJjSLcu5KMZNbIzotWpbAoYF5GbgZ9VIKueKc/edit#gid=162702674")

    town='Казань'
    r = requests.get(table[town])
    f = open(town+'.xlsx', 'wb')
    f.write(r.content)
    f.close()

    wb=openpyxl.load_workbook(town+'.xlsx', read_only=True, data_only=True)
    wb=wb["даты (копия) (копия)"]
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
    for house in info:
        if(len(info[house])!=0):
            for month in info[house]:
                if month_code[month]>datetime.datetime.now().month:
                    year=datetime.datetime.now().year+1
                else:
                    year=datetime.datetime.now().year
                for d in info[house][month]:
                    day=int(d)
                    date=datetime.date(year, m, day)
                    scip=0
                    col=30
                    for row in wb.rows:
                        if scip==0:
                            scip+=1
                            continue
                        if str(row[col].value).split(' ')[0]==str(date):
                            for r in wb.rows:
                                if (r[441].value).split("*", '')==house:
                                    DATA = {'requests': [{'repeatCell':
                                            {'range': 
                                                { 
                                                'startRowIndex': 0, # номер строки (нумерация с 0) с которой включительно будет применено форматирование
                                                'endRowIndex': 1, # номер строки до которой будет применено форматирование, не включительно
                                                    
                                                'startColumnIndex': 0, # номер столбца (нумерация с 0)…
                                                'endColumnIndex': 1
                                                },
                                            
                                            'cell':  {'userEnteredFormat': {'backgroundColor': {'red': 0}}},

                                            'fields': 'userEnteredFormat', # другие параметры форматирования ячейки будут сброшены
                                        }}
                                        ]}
                                    service.spreadsheets().batchUpdate(spreadsheetId = spreadsheet['spreadsheetId'], body=DATA).execute()


                

