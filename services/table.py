import os
import requests
import time
import openpyxl
import json
import gspread
import datetime
import httplib2
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient import discovery
from .full_name import FULL_NAME
from .google_authorization import google_data


def getData(row_number, col):
    """Формирование запроса для обновления гугл таблицы"""
    DATA = {'requests':
            [{'repeatCell':
              {'range':
               {"sheetId": 955783345,
                'startRowIndex': row_number,
                # номер строки (нумерация с 0) с
                # которой включительно будет применено
                # форматирование
                'endRowIndex': row_number + 1,
                # номер строки до которой будет применено
                # форматирование, не включительно

                # номер столбца (нумерация с 0)…
                'startColumnIndex': col,
                'endColumnIndex': col + 1
                },

               'cell': {
                   'userEnteredFormat': {'backgroundColor':
                                         {'red': 0,
                                          'green': 0,
                                          'blue': 128,
                                          }}},

               'fields': 'userEnteredFormat',
               # другие параметры форматирования ячейки будут
               # сброшены
               }}
             ]}
    return DATA


def tableUpdate(DATA, service):
    """Обновление гугл таблицей"""
    quot_limit = True
    while quot_limit:
        try:
            service.spreadsheets().batchUpdate(
                spreadsheetId='1JIstqYbaPS6ZkzbH7AmZ0xeb7VbMpmA6GrhPiZ5r5iY',
                body=DATA).execute()
            quot_limit = False
        except BaseException:
            time.sleep(5)


def tableDataUpdate(row_number, sheet, house):
    """Обновление последней даты обновления дома"""
    print(sheet)
    quot_limit = True
    while quot_limit:
        try:
            sheet.update_cell(row_number + 1, 27,
                str(datetime.datetime.now().date()))
            print(house + ' Update')
            quot_limit = False
        except BaseException:
            print("Quot limit")
            time.sleep(5)
    


def getCurrentDate(info, phone, house):
    """Формирование даты из сообщения"""
    month_code = {
        'январь': 1,
        'февраль': 2,
        'март': 3,
        'апрель': 4,
        'май': 5,
        'июнь': 6,
        'июль': 7,
        'август': 8,
        'сентябрь': 9,
        'октябрь': 10,
        'ноябрь': 11,
        'декабрь': 12,
    }
    year = 0
    month = 0
    day = 0
    current_date_list=[]
    for month_ in info[phone][house]:
        if len(info[phone][house][month_]) != 0:
            month = month_code[month_]
            if month_code[month_] < datetime.datetime.now().month:
                year = datetime.datetime.now().year + 1
            else:
                year = datetime.datetime.now().year
            last_valid_day = 0
            for day_ in info[phone][house][month_]:
                if last_valid_day != 0 and int(day_) < last_valid_day:
                    break
                last_valid_day = int(day_)
                day = int(day_)
                current_date = datetime.date(year, month, day)
                current_date_list.append(current_date)
    return current_date_list

def booking_update(row_number, col, service, row_, sheet, house,
                   excel_house, full_name):
    """Обнволение брони"""
    if str(excel_house.value) == full_name:
        DATA = getData(row_number, col)
        reserve_color_list = [
            'FF38761D', 'FF93C47D',
            'FF000080',
        ]
        if row_[col].fill.fgColor.rgb in reserve_color_list:
            return True
        update_flag = 1
        tableUpdate(DATA, service)
        tableDataUpdate(row_number, sheet, house)
        return True
    return False


def table(info, phone, wb):

    full_name = FULL_NAME
    google_table = google_data()
    service = google_table[0]
    sheet = google_table[1]

    for house in info[phone]:
        if house == '8казанка':
            continue
        if len(info[phone][house]) != 0:
            current_date_list = getCurrentDate(info, phone, house)
        else:
            continue
            #current_date = (datetime.datetime.now() - datetime.timedelta(days=2)).date()
        for current_date in current_date_list:
            try:
                if current_date < datetime.datetime.now().date():
                    # Если найденная дата меньше сегодняшней,
                    # то пропускаем ее
                    continue
            except:
                continue
            row_skeep = 0
            col = 30
            stop = False
            date_list = wb["даты"]
            print(house+' '+str(current_date))
            for row in date_list.rows:
                if row_skeep == 0:
                    row_skeep += 1
                    continue
                while not stop:
                    excel_data = str(row[col].value).split(' ')[0]

                    if excel_data == str(current_date):
                        row_number = -1

                        for row_ in date_list.rows:
                            row_number += 1

                            if booking_update(row_number, col, service, row_,
                                            sheet, house, row_[27], full_name[
                                                phone][house]):
                                stop = True
                                break
                    col += 1
                break
