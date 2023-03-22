import threading
import time
import requests

import json



def data_from_mono():
    print('Take date from NBU started')
    url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
    response = requests.get(url)
    data = json.loads(response.text)
    for item in data:
        if item['r030'] == 840:
            print("Курс USD покупки по НБУ:", item['rate'])
            a = item['rate']
            print("=====================")
    return a


def data_from_privat():
    print('Take date from Privat started')
    url = "https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5"
    response = requests.get(url)
    data = json.loads(response.text)
    for item in data:
        if item['ccy'] == 'USD':
            print("Курс USD покупки в Приваті:", item['buy'])
            b = item['buy']
            print("=====================")

    return b


def compare_exchange_rates():
    a = data_from_mono()
    b = data_from_privat()
    a1 = float(a)
    b1 = float(b)
    if a1 > b1:
        print("Курс USD покупки в НБУ вищий за курс покупки в Приваті")
    elif a1 < b1:
        print("Курс USD покупки в Приваті вищий за курс покупки в НБУ")
    else:
        print("Курс USD покупки в НБУ та Приваті однаковий")

function1 = threading.Thread(target=data_from_mono)
function2 = threading.Thread(target=data_from_privat)
function3 = threading.Thread(target=compare_exchange_rates)

function1.start()
function2.start()
function2.join()
function3.start()
