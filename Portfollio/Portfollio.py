from Execution.Execution import Execution

class Portfollio:
    def __init__(self,coin_number,principal,data):
        self.coin_number = coin_number
        self.principal = principal
        self.buy_amount = 10000#开单金额
        self.sell_amount = 10000
        self.data = data
        self.trade_sigle = 'None'
        self.position = ( coin_number * self.data.iat[-1,2] ) / self.principal
        self.judge_position = 0.5

    def position_control(self):
        print(self.data)
        for indx, row in self.data.iterrows():
            if((row['buy_index'] > 0) and (row['buy_index'] > row['sell_index']) and (self.judge_position > self.position)):
                self.buy()
            if((row['sell_index'] > 0) and (row['sell_index'] > row['buy_index']) and (self.position>0)):
                self.sell()
        return {'coin_number':self.coin_number,'principal':self.principal}

    def buy(self):
        sigle = 'buy'
        self.Execution = Execution(sigle,self.buy_amount,self.sell_amount,self.data,self.principal,self.coin_number)
        result = self.Execution.excu()
        self.coin_number = result['coin_number']
        self.principal = result['principal']

    def sell(self):
        sigle = 'sell'
        self.Execution = Execution(sigle,self.buy_amount,self.sell_amount,self.data,self.principal,self.coin_number)
        result = self.Execution.excu()
        self.coin_number = result['coin_number']
        self.principal = result['principal']