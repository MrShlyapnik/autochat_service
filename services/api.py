import requests
import datetime


def api_ls():
    headers = {
        'X-Private-Api-Token':
            '0505dcbab77f0071ce254a246f2b8b89c07ce0ae0cd919ece7bbea373c37c7301a4ecc3a0e2f39e5fb60e2d7471fb1e692369ca9e29978191b67f20b1260c9c2',
    }
    pact_id = '48455'  # id pact пользователя
    response = requests.get("https://api.pact.im/p1/companies/48455/channels",
                            headers=headers).json()
    owner_phone = [
        '79053116753', '79063257387', '79600363975', '79047619866',
        '79656012318', '79872974084', '79274226911', '79050212617',
        '79196237446', '79600482261', '79377772077', '79274180728',
        '79600323247', '79172290723', '79196224788', '79274358985',
        '79377771034', '79872711910', '79510675675', '79178670299',
        '79600421404', '79867124227', '79510675675', '79625515760',
        '79172795166', '79872975991', '79053129769', '79872970333',
        '79047648223', '79172850892', '79196381354', '79061155445',
    ]
    # Формат даты  date='2020-09-23 01:00:00'

    date_period = (datetime.datetime.now() - datetime.timedelta(seconds=30000))
    control_date = date_period

    messages_array = {}
    for number in owner_phone:
        count = 0
        messages_array[number] = []
        data = {
            'provider': 'whatsapp',
            'phone': number,
        }
        response = requests.post(
            'https://api.pact.im/p1/companies/' + pact_id + '/conversations',
            headers=headers, data=data).json()
        chat_id = response['data']['conversation']['external_id']
        response = requests.get(
            "https://api.pact.im/p1/companies/" +
            pact_id +
            "/conversations"
            "/" +
            str(chat_id) +
            "/messages?sort_direction=desc",
            headers=headers).json()

        for message in response['data']['messages']:
            message_time = message['created_at'].replace("T", " ").replace(
                "Z", "").split('.')[0]
            message_time = datetime.datetime.strptime(message_time,
                                                      '%Y-%m-%d %H:%M:%S')

            if message_time > control_date:
                count += 1
                messages_array[number].append(message['message'])
                print(message_time)
                current_time = (message_time)
                print("Время сообщения " + str(current_time))
            else:
                continue
        print('Собственник ' + number)
        print("Количество новых сообщений за последнее время " + str(count))
    return messages_array


def api_chat():
    owner_phone = [
        '79872971476-1481554579@g.us', '79178767741-1419363809@g.us',
        '79655807679-1585037693@g.us', '79655888066-1485072828@g.us',
        '79655896555-1527783737@g.us', '79046764175-1568197083@g.us',
        '79172591019-1564744795@g.us', '79046764175-1528129775@g.us',
        '79520308800-1503831959@g.us', '79872360002-1599913260@g.us',
        '79600510471-1579437045@g.us', '79172998115-1568958489@g.us',
        '79270394387-1557135797@g.us', '79046764175-1569163276@g.us',
        '79272447447-1580997756@g.us', '79655995118-1496687048@g.us',
    ]
    date_period = (datetime.datetime.now() - datetime.timedelta(
        seconds=20000)).timestamp()
    control_date = date_period
    messages_array = {}
    for number in owner_phone:
        messages_array[number] = []

        response = requests.get(
            'https://api.chat-api.com/instance175111/messages?token'
            '=s5xri89wo7jl37dk',
            params={
                "chatId": number,
                "lastMessageNumber": 100,
                "last": 1,
            }
        ).json()
        message_count = 0

        for message in response['messages']:
            message_time = float(message['time'])

            if message_time > control_date:
                messages_array[number].append(message['body'])
                message_count += 1
                current_time = datetime.datetime.fromtimestamp(message_time)
                print("Время сообщения " + str(current_time))
            else:
                continue
        print('Собственник ' + number)
        print("Количество новых сообщений за последнее время " + str(
            message_count))
    return messages_array
