from Portfollio.Portfollio import Portfollio
from multiprocessing import  Manager,Pool
from Strategy_fun import *
class Strategy:
    def __init__(self,data,coin_number,principal):
        self.buy_index = 0
        self.sell_index = 0
        self.coin_number = coin_number
        self.principal = principal
        self.data = data

    def analysis(self):
        with Manager() as manager:
            index = manager.dict()
            pool = Pool(processes=2)
            pool.apply_async(func=macd,args=(self.data,index))
            pool.apply_async(func=ma, args=(self.data, index))
            pool.close()
            pool.join()
            ######判断参数条件
            self.data['macd'] = index['macd']['macd']
            self.data['macdhist'] = index['macd']['macdhist']
            self.data['macdsignal'] = index['macd']['macdsignal']
            self.data['ma'] = index['ma']
            recod = [{'buy_index':[]},{'sell_index':[]}]#初始化装buy_index和sell_index 的列表
            for  indx, row in self.data.iterrows():
                if(row['macdhist']>0):
                    self.buy_index_adjust(60)
                if(row['macdhist']<0):
                    self.sell_index_adjust(60)

                if(row['close']>row['ma']):
                    self.buy_index_adjust(40)
                if(row['close']<row['ma']):
                    self.sell_index_adjust(40)
                recod[0]['buy_index'].append(self.buy_index)
                recod[1]['sell_index'].append(self.sell_index)
                self.buy_index = 0
                self.sell_index = 0
            self.data['buy_index'] = np.array(recod[0]['buy_index'])
            self.data['sell_index'] = np.array(recod[1]['sell_index'])
            self.Portfollio = Portfollio(self.coin_number,self.principal,self.data)
            return self.Portfollio.position_control()


    def buy_index_adjust(self,number):
        self.buy_index += number

    def sell_index_adjust(self,number):
        self.sell_index += number


