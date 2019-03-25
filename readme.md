# BakTst_Org
中文reademe：传送门
>Introduction: BakTst_Org is a prototype of the backtesting system used by my own bitcoin quantitative trading.
----
This readme is mainly divided into the following parts:
* What kind of person is suitable for studying BakTst_Org?
* Library to be imported
* BakTst_Org's framework and various modules of the framework
* How to use BakTst_Org
* Extension
* Question
* Results map
* Some ideas for the future
* Thanks list
---
### What kind of person is suitable for studying BakTst_Org?
BakTst_Org is just a prototype, the amount of code is not large, about four hundred lines, very simple. But what is needed is still there, such as: multi-process, simulation of the actual output parameters of the real open position, data acquisition crawler, simulation of the real opening process.

So the right people include:
* Primary learning python programming people
* Script developer
* Financial enthusiasts
* Quantify traders
### Library to be imported
Talib, multiprocessing, pandas, json, numpy, time, requests
### BakTst framework and introduction to each module of the framework
BakTst_Org mainly divides 6 modules, which are:
* craw (crawler module)
* Feed (data acquisition module)
* Strategy (Strategy Module)
* Portfollio (position management module)
* Execution (order execution module)
* main function
#### craw
This module is a separate module, the API called is the bittrex api, which is mainly used to obtain transaction record data and then write to the txt file.

Api: https://api.bittrex.com/api/v1.1/public/getmarkethistory?market=usdt-btc
If you want to modify the transaction data of the acquired currency, you only need to modify the last *usdt-btc* transaction pair. For example: usdt to ltc, you can modify it to *usdt-ltc*.

The time limit for getting is 60 requests per minute, so a `time.sleep(1)` is added.

The deposited data is divided into two files, one is the complete transaction data, and the other is the highest price, the lowest price, the opening price, the closing price, the transaction volume, the time, and the currency data every 3 minutes.

For the format of the data, please refer to the two txt files in the crash directory.

#### Feed

This module is used as a data transfer module for BakTst, receives the initialized data, and then passes it to the entire backtesting system. Received data:
* data: The highest price, lowest price, opening price, closing price, time, etc. of the transaction for three minutes. The format is dataframe.
* coin_number: The number of coins owned by the position initialization.
* principal: principal
#### Strategy
This module is used as the policy execution module of BakTst_Org, receives the transaction data transmitted from the feed module, and then performs quantitative analysis through this module, and then sets buy_index (buy index) and sell_index (sell index) to feedback the transaction. The trend is to finally transfer the data to the Portfollio module. The Strategy.py file writes logical decisions, the Strategy_fun.py file writes two strategy class functions, and a format conversion function.

#### Portfollio
This module is used as a position management module for BakTst_Org. Although we have just judged the buying and selling trend, if we set a standard and no longer open positions after more than 0.5 positions, then this module will play a limiting role. At the same time, the opening and selling signals will be sent to the next one. Execution module. Explain the meaning of the next few parameters:
* buy_amount and sell_amount: The fixed billing amount may not be fixed in the real situation, but it is only a prototype, and the position of these two parameters is temporarily left there.
* trade_sigle: trading signal, ‘sell’ is for sale, ‘buy’ is for purchase, ‘None’ is for inaction, in subsequent code, this is a judgment basis.
* judge_position: position, the value is less than 1.

#### Execution
This module is used as an order execution module for BakTst_Org to simulate the user's actual billing situation and will eventually return a total profit and loss situation. Explain the meaning of the next few parameters:
* tip: handling fee.
* buy_flap: The slippage of the purchase.
* sell_flap: The slippage of the sale.
* buy_last_price and sell_last_price: the last traded price of the trade.

#### Main function
Convert the data of the txt document into the data of the dataframe format and pass it to the whole system. Finally, the system will return a final number of coins and the number of principals. The main function compares the initial and final prices to calculate the final profit and loss. The meaning of the last printed parameter:
* earn: earn.
* lose: loss.
* balance: no loss, no profit.

### How to use BakTst_Org
* First you need to collect data using the craw.py file in the craw module alone.
* Run the BakTst_Org.py file to see the output.
###Extension
* Dynamic change value: In addition to some values ​​that need to be fixed, such as the principal, position, handling fee, there are some values ​​that can be dynamically changed, such as slippage, single billing amount.
* Function of the strategy class: Although I just wrote two, you can add more, just add these methods to the Strategy_fun.py file.
###Question
Mainly some problems encountered in the development process, give two examples:
* I have encountered a problem with naming coverage. **open**, I encountered this problem when I wrote `with open (addr , 'w') as w:` and set the opening price name 'open'.
* Multi-process, I use the process pool solution. But when calling the methods in the class, I found out that I can't call them. Finally, I can call these methods that need to run multiple processes on the outside.
### Some ideas for the future
I will publish this prototype, but for everyone to learn from, if it is used to really do quantitative transactions, it is not enough. So next, I will develop a quantitative trading system that connects with the real disk based on BakTst_Org.
### Thanks list
* Thanks to everyone in 慢雾区远不止狗币技术群, helped me solve the programming problems.
* Thanks to greatshi, a big deal in the field of quantitative trading. I didn't have any experience in developing over-trading systems before, and greatshi patiently answered and guided me how to develop BakTst_Org, thank you.