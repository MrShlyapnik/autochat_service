import requests
import datetime
def api_ls():
    headers = {
        'X-Private-Api-Token': '0505dcbab77f0071ce254a246f2b8b89c07ce0ae0cd919ece7bbea373c37c7301a4ecc3a0e2f39e5fb60e2d7471fb1e692369ca9e29978191b67f20b1260c9c2',
    }
    # data={
    #     'provider':'whatsapp',
    #     'phone':"client",
    # }
    response=requests.get("https://api.pact.im/p1/companies/48455/channels", headers=headers).json()
    owner_phone=[
        '79053116753',
        '79063257387',
        '79600363975',
        '79047619866',
        '79656012318',
        '79872974084',
        '79274226911',
        '79050212617'

    ]
    date='2020-09-23 01:00:00'
    date=datetime.datetime.now()-datetime.timedelta(seconds=36000)
    control_date=date
    messages_array={}
    for number in owner_phone:
        print(number)
        messages_array[number]=[]
        data={
        'provider':'whatsapp',
        'phone': number,
        }
        pact_id='48455'
        response = requests.post('https://api.pact.im/p1/companies/'+pact_id+'/conversations', headers=headers, data=data).json()
        id=(response)
        id=int(id['data']['conversation']['external_id'])
        response=requests.get("https://api.pact.im/p1/companies/"+pact_id+"/conversations/"+str(id)+"/messages?sort_direction=desc", headers=headers).json()
        print('pact')
        print(len(response['data']['messages']))
        for message in response['data']['messages']:
            message_time=message['created_at'].replace("T", " ").replace("Z", "").split('.')[0]
            message_time=datetime.datetime.strptime(message_time, '%Y-%m-%d %H:%M:%S')
            print(message_time)
            print(control_date)
            if message_time>control_date:
                
                if message['income']:
                    # print(message['message'])
                    print(message['message'])
                    messages_array[number].append(message['message'])
            else:
                continue
    return messages_array


def api_chat():
    
    owner_phone=[
        '79872971476-1481554579@g.us',
        '79178767741-1419363809@g.us',
         '79655807679-1585037693@g.us',
         '79655888066-1485072828@g.us',
         '79655896555-1527783737@g.us',

    ]
    date='2020-09-23 01:00:00'
    date=(datetime.datetime.now()-datetime.timedelta(seconds=36000)).timestamp()
    control_date=date
    messages_array={}
    for number in owner_phone:
        messages_array[number]=[]
        
        response=requests.get(
           'https://api.chat-api.com/instance175111/messages?token=s5xri89wo7jl37dk',
            params=
                {
                    'chatId':number,
                }
            
        ).json()
        # print(response)
        for message in response['messages']:
            message_time=int(message['time'])
            if message_time>control_date:
                if message['fromMe']==False:
                    print(message['body'])
                    messages_array[number].append(message['body'])
            else:
                continue
    return messages_array