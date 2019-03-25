import json
from pandas import DataFrame
from Feed.Feed import Feed
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def readfile(addr):
    result = []
    with open(addr, 'r') as r:
        for i in r.readlines():
            if (len(i) > 3):
                result.append(json.loads(i))
    return result

if __name__ == '__main__':
    result = readfile(r'/craw/data2.txt')
    coin_number = 5#仓位拥有币数
    principal = 1000000#本金
    initals = {'coin_number':coin_number,'principal':principal,'inital_retail_price':result[0]['close']}
    col = ['data', 'open_price', 'close', 'low', 'high', 'volume', 'code']
    data_frame = DataFrame(columns=col)
    for i in result:
        data_frame  = data_frame.append(i,ignore_index=True)
    feed = Feed(data_frame, coin_number, principal)
    msg = feed.send_data()
    coin_number = msg['coin_number']
    principal = msg['principal']
    print('coin_number:'+str(coin_number)+',principal:'+str((principal)))
    last_retail_price = data_frame.iat[-1,2]
    totle_change_money = round((initals['coin_number'] * initals['inital_retail_price'] + initals['principal']) - (coin_number * last_retail_price + principal),3)
    if(totle_change_money>0):
        print('earn：' + str(totle_change_money))
    elif(totle_change_money<0):
        print('lose：' + str(totle_change_money))
    elif(totle_change_money == 0):
        print('balance')




