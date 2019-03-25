# BakTst_Org
>介绍：BakTst_Org 是我自己写的一个比特币量化交易会用到的回测系统的框架雏形。
----
本篇readme主要分成以下几个部分：
* BakTst_Org 适合哪些人看
* 需要导入的库
* BakTst_Org 的框架以及对于框架各个模块的介绍
* 如何使用BakTst_Org
* 扩展
* 疑问
* 结果图
* 未来的一些想法
* 感谢名单
---
### BakTst_Org 适合哪些人看
BakTst_Org只是一个雏形，代码量不大，大概四百行左右，很简单，但是该有的还是会有，如：多进程、模拟真实开仓的传入输出参数、数据获取爬虫、模拟真实的开仓流程。

所以适合的人群包括：
* 初级学习python编程的人
* 脚本开发者
* 金融爱好者
* 量化交易人群
### 需要导入的库
talib、multiprocessing、pandas、json、numpy、time、requests
### BakTst 的框架以及对于框架各个模块的介绍
BakTst_Org主要划分了6个模块，分别是：
* craw 爬虫模块
* Feed 数据获取模块
* Strategy 策略模块
* Portfollio仓位管理模块
* Execution 订单执行模块
* 主函数
#### craw
这个模块是单独使用的模块，调用的api是bittrex的api，主要用于获取交易记录数据，然后写入txt文档。

api：https://api.bittrex.com/api/v1.1/public/getmarkethistory?market=usdt-btc
如果想要修改获取的币种的交易数据，只需要修改最后的*usdt-btc*交易对即可，比如：usdt对ltc，可以修改成*usdt-ltc*。

获取的时间限制是一分钟60次请求，所以会加上一个`time.sleep(1)`。

存入数据分为两个文件，一个是完整的交易数据，另外一个是每3分钟的最高价、最低价、开盘价、收盘价、交易量、时间、币种的数据。

关于数据的格式问题，请参考craw目录下的两个txt文件。

#### Feed

这个模块是作为BakTst的数据传入模块，接收初始化的数据，然后传入整个回测系统。接收的数据：
* data: 交易三分钟的最高价、最低价、开盘价、收盘价、时间等的数据，格式为dataframe
* coin_number: 仓位初始化拥有的币数。
* principal: 本金
#### Strategy
这个模块是作为BakTst_Org的策略执行模块，接收从Feed模块中传过来的交易数据，再通过本模块进行量化分析，然后设置buy_index(买的指数)和sell_index(卖的指数)，来反馈出交易的趋向，最后将数据传送到Portfollio模块。Strategy.py 文件里写的是逻辑判断，Strategy_fun.py 文件里写的是两个策略类的函数，和一个格式转化函数。

#### Portfollio
这个模块是作为BakTst_Org的仓位管理模块。虽然，刚才判断出买卖趋势了，但是如果设定一个标准，超过0.5的仓位后就不再进行开仓，那么这个模块，就起着限制作用，同时，将开仓，卖出的信号发送到下一个Execution模块。说明下几个参数的含义：
* buy_amount和sell_amount：固定的开单金额，真实情况下可能不会这样，固定，但是目前只是雏形，随意暂时留这两个参数的位置在那里。
* trade_sigle：交易信号，‘sell’ 为卖，‘buy’为买，‘None’为不作为，在后续代码中，这是一个判断依据。
* judge_position：仓位，数值小于1。

#### Execution
这个模块是作为BakTst_Org的订单执行模块，模拟用户真实开单情况，并且最后会返回一个总的盈亏情况。说明下几个参数的含义：
* tip：手续费。
* buy_flap：购买的滑点。
* sell_flap: 卖的滑点。
* buy_last_price 和 sell_last_price：交易的最后成交价。

#### 主函数
将txt文档的数据，转换成dataframe格式的数据，传入整个系统中，最后系统会返回一个最后的拥有的币数，以及本金数。主函数再对比最初和最后的价格，来算出最后的盈亏。最后打印出来的参数的含义：
* earn：赚
* lose：亏
* balance：不亏不赚

### 如何使用BakTst_Org
* 首先需要单独使用craw模块中的craw.py 文件收集数据。
* 运行BakTst_Org.py 文件，查看输出。
### 扩展
* 动态变化值：除了一些需要固定设置的值，比如本金，仓位，手续费，还有些可以动态变化的值，比如滑点，单笔开单金额。
* 策略类的函数：虽然我只是写了两个，你可以增加更多，只需要将这些方法添加在Strategy_fun.py 文件里。
### 疑问
主要是一些开发过程中遇到的问题，举两个例子：
* 遇到过一次命名覆盖的问题。**open**，我写`with open (addr , 'w') as w:` 和设置开盘价 open 的时候，遇到了这个问题。
* 多进程，我采用的进程池的方案。但是调用类里的方法时，却发现怎么也不能调用，最后将这些需要跑多进程的方法，放在外部，就可以调用了。
###结果图
### Results map
![result1](https://github.com/xiaoyao153379/BakTst_Org/blob/master/picture/1.png?raw=true "result")
![result2](https://github.com/xiaoyao153379/BakTst_Org/blob/master/picture/2.png?raw=true "result")
### 未来的一些想法
我将这个雏形发表出来，只是供大家学习参考，如果拿来真正做量化交易，还不够。所以接下来，我将再BakTst_Org的基础上，开发出一个与真实盘相接的量化交易系统。
### 感谢名单
* 感谢**慢雾区远不止狗币技术群**的各位，帮助我解决了编程方面的问题。
* 感谢greatshi，一个量化交易领域的大佬。我之前并没有开发过量化交易系统方面的经验，greatshi很耐心的回答并且指导我如何开发出BakTst_Org，多谢。





