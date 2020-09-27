from .table import table
import openpyxl
import requests
def parser(message, phone,wb):
    # f=open('text.txt', encoding="utf-8")
    # text=f.read()
    # f.close()
    text=message
    months=['январь','февраль','март','апрель','май',
        'июнь','июль','август','сентябрь',
        'октябрь','ноябрь','декабрь',
    ]
    message=text.lower()
    for m in months:
        message=message.replace(m, ' ' +m+' ')
    message=message.replace("-", "")
    message=message.replace("Занятые даты", " ")
    message=message.replace("Занятые даты!", " ")
    message=message.replace("занятые даты!", " ")
    message=message.replace("!", " ")
    message=message.replace(";", " ")
    message=message.replace(".", "")
    message=message.replace("🏡", ' ')
    message=message.replace("✅", ' ')
    message=message.replace("⛔", ' ')
    message=message.replace("🧸", ' ')
    message=message.replace("🔥", ' ')
    message=message.replace("\n", " ")
    message=message.replace(":", " ")
    message=message.replace(",", " ")
    message=message.replace("(", " ")
    message=message.replace(")", " ")
    message=message.replace("     ", " ")
    message=message.replace("    ", " ")
    message=message.replace("   ", " ")
    message=message.replace("  ", " ")
    message=message.replace("*", " ")
    new_formating_message=""
    info={
    '79053116753':
    {
        'домбогородское':{},
            'домшапши':{},
    },
    '79063257387':
    {
        'малый':{},
        'большой':{},
    },
    '79600363975':
    {
        'зеленыйминдаль':{},
        'салмачи':{},
    },
    '79377771034':
    {
        'деревянный':{},
        'кирпичный':{},
    },
    '79047619866':
    {
        'замок':{},
        'сруб':{},
        'дворец':{},
    },
    '79656012318':
    {
        'бавария':{},
        
        'панорама':{},
    },
    '79872711910':
    {
        'конcтантиновка':{},
    },
    '79510675675':
    {
        'пулиха':{}
    },
    '79872974084':
    {
        'амалый':{},
        'бсредний':{},
        'вбольшой':{},
    },
    '79274226911':
    {
        'чайка1':{},
        'чайка2':{},
    },
    '79050212617':
    {
        'дом':{},
        'русская':{},
        'охотничья':{},
        'берег':{},
        'парк':{},
    },
    '79196237446':
    {
        "улодносторонканоксинская":{}
    },
    '79600482261':
    {
        'черемшановая23':{}
    },
    '79377772077':
    {
        'калинино':{}
    },
    '79274180728':
    {
        'привольный':{}
    },
    '79600323247':
    {
        "мал56":{},
        "малбас60":{},
        "больш58":{},
        "сред54":{},
        "новый66":{},
        "нов66":{},

    },
    '79172290723':
    {
        "дачная128":{}
    },
    '79196224788':
    {
        'мира141':{}
    },
    '79274358985':
    {
        'беломорская54':{}
    },
    '79872971476-1481554579@g.us':
    {
        'к1':{},
            'к3':{},
            'к4':{},
    },
    '79178767741-1419363809@g.us':
    {
        'банкетныйзал':{},
        '1рыцарский':{},
            '2vip':{},
            '3классический':{},
            '4восточный1':{},
            '5восточный2':{},
            '6японский':{},
            '7гостевой':{},
            '8казанка':{},

    },
    '79655807679-1585037693@g.us':
    {
        'царский':{},
            'сосновый':{},
            'панорама':{},
            'апартаменты':{},
             'дятлово':{},
    },
    '79655888066-1485072828@g.us':
    {
        '3новый':{},
        'малый':{},
            'большой':{},
    },
    '79655896555-1527783737@g.us':
    {
        'малый':{},
            'большой':{},
    },
    '79046764175-1568197083@g.us':
    {
        'литвинова1а':{}
    },
    '79172591019-1564744795@g.us':
    {
        'набережная3':{},
        'нагоре/141':{},
        'набережная4':{},
    },
    '79046764175-1528129775@g.us':
    {
        'утренняя8а':{}
    },
    '79520308800-1503831959@g.us':
    {
        'мичурина117':{}
    }
    }
    # info={
        
    #         'домброгородское':{},
    #         'домшапши':{},
    #         'дятлово':{},
    #         'набережная3':{},
    #         'нагоре/141':{},
    #         'набережная4':{},
    #         'малый':{},
    #         'большой':{},
    #         'зеленыйминдаль':{},
    #         'деревянный':{},
    #         'кирпичный':{},
    #         'замок':{},
    #         'сруб':{},
    #         'дворец':{},
    #         'царский':{},
    #         'сосновый':{},
    #         'панорама':{},
    #         'апартаменты':{},
    #         'бавария':{},
    #         'контсантиновка':{},
    #         'к1':{},
    #         'к3':{},
    #         'к4':{},
    #         'дом':{},
    #         'русская':{},
    #         'охотничья':{},
    #         'берег':{},
    #         'парк':{},
    #         'кощаково':{},
    #         'занято':{},
    #         '8казанка':{},
    #         'банкетныйзал':{},
    #         '1рыцарский':{},
    #         '2vip':{},
    #         '3классический':{},
    #         '4восточный1':{},
    #         '5восточный2':{},
    #         '6японский':{},
    #         '7гостевой':{},
    #         'а':{},
    #         'б':{},
    #         'в':{},
    #         'г':{},
    #         'салмачи':{},
    #         'новый':{},
    #         'мал':{},
    #         'малбас':{},
    #         'сред':{},
    #         'больш':{},
    #         'амалый':{},
    #         'бсредний':{},
    #         'вбольшой':{},
    #         'чайка1':{},
    #         'чайка2':{},

    #     }

    info1={
            'черемшановая 23':{},
            'дом богородское':{},
            'дом шапши':{},
            'дятлово':{},
            'набережная 3':{},
            'на горе / 141':{},
            'набережная 4':{},
            'малый':{},
            'большой':{},
            'зеленый миндаль':{},
            'деревянный':{},
            'кирпичный':{},
            'замок':{},
            'сруб':{},
            'дворец':{},
            'царский':{},
            'сосновый':{},
            'панорама':{},
            'апартаменты':{},
            'бавария':{},
            'контсантиновка':{},
            'к1':{},
            'к3':{},
            'к4':{},
            'дом':{},
            'русская':{},
            'охотничья':{},
            'берег':{},
            'парк':{},
            'кощаково':{},
            'занято':{},
            '8 казанка':{},
            'банкетный зал':{},
            '1рыцарский':{},
            '2 vip':{},
            '3классический':{},
            '4 восточный 1':{},
            '5восточный 2':{},
            '6японский':{},
            '7гостевой':{},
            'а':{},
            'б':{},
            'в':{},
            'г':{},
            'салмачи':{},
            'новый':{},
            'мал':{},
            'мал.бас':{},
            'сред':{},
            'больш':{},
            'а малый':{},
            'б средний':{},
            'в большой':{},
            'чайка1':{},
            'чайка2':{},
            'ул односторонка ноксинская':{},
            'мира 141':{},
            'беломорская 54':{},
            'дачная 128':{},
            'утренняя 8а':{},
            'мичурина117':{},
            'больш 58':{},
            'малбас 60':{},
            'мал 56':{},
            'нов 66':{},
            'новый 66':{},
            'сред 54':{}


        }

    # print(info)
    # print(message)
    for i in info1:
        message=message.replace(i, i.replace(" ", ""))
    message=message.replace("     ", " ")
    message=message.replace("    ", " ")
    message=message.replace("   ", " ")
    message=message.replace("  ", " ")
    # print(message)
    house=""
    month=""
    if len(info[phone])==1:
        for h in info[phone]:
            house=h
    if phone=='79600323247':
        for word in message.split(" "):
           
            if word not in info[phone]:
                if word.lower() not in months:
                    if word.isdigit():
                        if int(word)<=0 or int(word)>=32:
                            continue
                    else:
                        continue
                else:
                    month=word.lower()
                    continue
            if word in info[phone]:
                house=word
                continue
            else:
                if house!="":
                    # print(house)
                    if (word.lower() in months):
                    
                       
                        try:
                            print(len(info[phone][house][month]))
                        except:
                            info[phone][house][month]=[]
                            house=""
                    
                    else:
                        try:
                            
                          
                            try:
                                info[phone][house][month].append(word)
                            except:
                                info[phone][house][month]=[]
                                info[phone][house][month].append(word)
                        except:
                            print("Error")
    else:
        for word in message.split(" "):
            
            if word not in info[phone]:
                if word.lower() not in months:
                    if word.isdigit():
                        if int(word)<=0 or int(word)>=32:
                            continue
                    else:
                        continue
                else:
                    month=word.lower()
            if word in info[phone]:
                house=word
            else:
                if house!="":
                    if (word.lower() in months):
                    
                        # print(house)
                        # print(month)
                        try:
                            print(len(info[phone][house][month]))
                        except:
                            info[phone][house][month]=[]
                    
                    else:
                        try:
                            
                            
                            info[phone][house][month].append(word)
                        except:
                            pass
    # print(info)
    for h in info[phone]:
        if len(info[phone][h])!=0:
            print(h+':    ')
            for t in info[phone][h]:
                if(len(info[phone][h][t])>0):
                    print(str(t)+"             "+str(info[phone][h][t]))
    
    table(info, phone,wb)