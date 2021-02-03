import json
import gspread
import httplib2
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient import discovery


def google_data():
    table = {
        'Казань': 'https://docs.google.com/spreadsheets/d'
        '/1JIstqYbaPS6ZkzbH7AmZ0xeb7VbMpmA6GrhPiZ5r5iY/export?format=xlsx&id=1JIstqYbaPS6ZkzbH7AmZ0xeb7VbMpmA6GrhPiZ5r5iY',
        'Москва': 'https://docs.google.com/spreadsheets/d'
        '/1dhTz3mTVYd1y9KqdCd1KUbY0AmyaZhVdOQ6qTX9b9C4/export?format=xlsx&id=1dhTz3mTVYd1y9KqdCd1KUbY0AmyaZhVdOQ6qTX9b9C4',
    }
    # получаем доступ к гугл таблице
    # json credentials you downloaded earlier
    json_key = json.load(open('creds.json'))
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        'creds.json', scopes=scope)
    httpAuth = credentials.authorize(httplib2.Http())
    service = discovery.build('sheets', 'v4', http=httpAuth)

    file = gspread.authorize(credentials)  # authenticate with Google
    sheet = file.open_by_url(
        "https://docs.google.com/spreadsheets/d/1JIstqYbaPS6ZkzbH7AmZ0xeb7VbMpmA6GrhPiZ5r5iY/edit#gid=955783345")
    return [service, sheet]
