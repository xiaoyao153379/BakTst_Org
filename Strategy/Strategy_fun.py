import talib
import numpy as np

def macd(data,index):
    close_arry = tranform_arry(data['close'])
    macd, macdsignal, macdhist = talib.MACD(close_arry, fastperiod=12, slowperiod=26, signalperiod=9)
    index['macd'] = {'macd':macd,'macdsignal':macdsignal,'macdhist':macdhist}

def ma(data,index):
    close_arry = tranform_arry(data['close'])
    index['ma'] = talib.MA(close_arry, timeperiod=10)

def tranform_arry(dataframe):
    close = [float(x) for x in dataframe]
    return np.array(close)
