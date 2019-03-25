import requests
import json
import time

def craw(url):
    flag = True
    while flag:
        try:
            result = json.loads(requests.get(url,timeout = 3).text)
            flag = False
            return result
        except:
            flag = True
            time.sleep(1)


url5 = 'https://api.bittrex.com/api/v1.1/public/getmarkethistory?market=usdt-btc'
history_id = []
history_oder = []
history_data = []
volume = 0.00
result = craw(url5)['result']
open_price = result[0]['Price']
low = result[0]['Price']
high = result[0]['Price']
close = result[0]['Price']
volume += result[0]['Quantity']
history_id.append(result[0]['Id'])
history_oder.append(result[0])
time.sleep(1)
number = 1
while True:
    result = craw(url5)['result']
    for i in result:
        if i['Id'] not in history_id:
            if(low>i['Price']):
                low = i['Price']
            if(high<i['Price']):
                high = i['Price']
            close = i['Price']
            volume += i['Quantity']
            history_id.append(i['Id'])
            history_oder.append(i)
    data = {'getmarkethistory':history_oder}
    history_data.append(data)
    history_oder = []
    number += 1
    if(number > 60):
        with open('data_all.txt','a') as w:
            w.write(json.dumps(history_data)+'\n')
        with open('data.txt','a') as ws:
            ws.write(json.dumps({'data':time.time(),'open_price':open_price,'close':close,'low':low,'high':high,'volume':volume,'code':'btc'})+'\n')
        open_price = result[0]['Price']
        close = result[0]['Price']
        low = result[0]['Price']
        high = result[0]['Price']
        number = 0
        volume += result[0]['Quantity']
        history_data = []
        history_id = []
    print(data)
    time.sleep(1)