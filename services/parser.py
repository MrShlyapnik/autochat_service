from table import table
import openpyxl
import requests
# def parser(message, id):
f=open('text.txt', encoding="utf-8")
text=f.read()
f.close()
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
message=message.replace(".", "")
message=message.replace("🏡", '')
message=message.replace("✅", '')
message=message.replace("⛔", '')
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
    
        'домброгородское':{},
        'домшапши':{},
        'дятлово':{},
        'набережная3':{},
        'нагоре/141':{},
        'набережная4':{},
        'малый':{},
        'большой':{},
        'зеленыйминдаль':{},
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
        '8казанка':{},
        'банкетныйзал':{},
        '1рыцарский':{},
        '2vip':{},
        '3классический':{},
        '4восточный1':{},
        '5восточный2':{},
        '6японский':{},
        '7гостевой':{},
        'а':{},
        'б':{},
        'в':{},
        'г':{},
        'салмачи':{},
        'новый':{},
        'мал':{},
        'малбас':{},
        'сред':{},
        'больш':{},
        'амалый':{},
        'бсредний':{},
        'вбольшой':{},
        'чайка1':{},
        'чайка2':{},

    }

info1={
    
        'дом брогородское':{},
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

    }


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
for word in message.split(" "):
    if word not in info:
        if word.lower() not in months:
            if word.isdigit():
                if int(word)<=0 or int(word)>=32:
                    continue
            else:
                continue
        else:
            month=word.lower()
    if word in info:
        house=word
    else:
        if house!="":
            if (word.lower() in months):
            
                # print(house)
                # print(month)
                info[house][month]=[]
            
            else:
                try:
                    
                    
                    info[house][month].append(word)
                except:
                    pass
for h in info:
    if len(info[h])!=0:
        print(h+':    ')
        for t in info[h]:
            if(len(info[h][t])>0):
                print(str(t)+"             "+str(info[h][t]))
table(info)