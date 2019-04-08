import json

class Execution:
    def __init__(self,sigle,buy_amount,sell_amount,data,principal,coin_number):
        self.sigle = sigle
        self.buy_amount = buy_amount #the amount of buying
        self.sell_amount = sell_amount #the amount of selling
        self.data = data
        self.principal = principal
        self.coin_number = coin_number
        self.tip = 0.0025#手续费
        self.buy_flap = 1#购买的滑点
        self.sell_flap = 1#卖的滑点
        self.buy_last_price = self.data.iat[-1,2] + self.buy_flap #买的成交价
        self.sell_last_price = self.data.iat[-1,2] - self.buy_flap #卖的成交价

    def excu(self):
        exchange_number = 0
        if(self.sigle == 'buy'):
            increase_coins_number = (self.buy_amount - self.buy_amount*self.tip) / + self.buy_last_price
            self.count_coin_number(increase_coins_number)
            self.count_principal((0.00000 - self.buy_amount))
            exchange_number = increase_coins_number
            print('action:buy,amount:' + str(increase_coins_number) + ',totle_money:' + str(
                self.buy_amount) + ',retail_price:' + str(self.buy_last_price))
            self.record(exchange_number,'buy')

        if(self.sigle == 'sell'):
            decrease_coin_number = (self.sell_amount - self.sell_amount*self.tip) / self.data.iat[-1, 2]
            self.count_coin_number((0.00000 - decrease_coin_number))
            self.count_principal(self.sell_amount)
            exchange_number = decrease_coin_number
            print('action:sell,amount:' + str(decrease_coin_number) + ',totle_money:' + str(
                self.sell_amount) + ',retail_price:' + str(self.sell_last_price))
            self.record(exchange_number,'sell')

        if(self.sigle == 'None'):
            return {'coin_number':self.coin_number,'principal':self.principal}
        return {'coin_number':self.coin_number,'principal':self.principal}


    def count_coin_number(self , vary_number):
        self.coin_number += vary_number

    def count_principal(self,vary_principal):
        self.principal +=  vary_principal

    def record(self,exchange_number,action):
        with open('record.txt','a') as w:
            w.write(json.dumps({'action':action,'price':self.data.iat[-1,2],'time':self.data.iat[-1,0],'number':exchange_number,'principal':self.principal,'coin_number':self.coin_number})+'\n')
        print('last: ' + str((self.data.iat[-1,2] * self.coin_number + self.principal)) + '\n')