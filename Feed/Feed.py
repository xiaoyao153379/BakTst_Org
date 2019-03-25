import Strategy.Strategy as Strategy

class Feed:
    def __init__(self,data,coin_number,principal):
        self.data = data
        self.coin_number = coin_number #仓位拥有币数
        self.principal = principal #本金

    def send_data(self):
        self.Strategy = Strategy.Strategy(self.data,self.coin_number,self.principal)
        return self.Strategy.analysis()