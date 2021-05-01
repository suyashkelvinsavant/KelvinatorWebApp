import grequests
import json
import time
from datetime import datetime
def data30():
    # with open('./json/stocksData/data30.json') as f:
    #    stData = json.load(f)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    with open('./website/json/stockList/stockList.json') as f:
        stockList = json.load(f)
    n=18
    aoa = []
    for i in range(0, len(stockList), n):
        aoa.append(stockList[i:i + n])
    sUrls=[]
    for slist in aoa:
        s='%2C'
        sUrls.append(f"https://query1.finance.yahoo.com/v7/finance/spark?symbols={s.join(slist)}&range=1mo&interval=30m")
    request = (grequests.get(u) for u in sUrls)
    result = grequests.map(request)
    sData = [r.json() for r in result]
    stData={}

    chartUrls=[]
    for symbol in stockList:
        chartUrls.append(f"https://query1.finance.yahoo.com/v7/finance/chart/{symbol}?range=1d&interval=30m")
    crequest = (grequests.get(cu) for cu in chartUrls)
    cresult = grequests.map(crequest)
    cData = [cr.json() for cr in cresult]
    chartData={}
    for stock in cData:
       chartData[f"{stock['chart']['result'][0]['meta']['symbol']}"]={"timestamp":stock['chart']['result'][0]['timestamp'],"close":stock['chart']['result'][0]['indicators']['quote'][0]['close'],"open":stock['chart']['result'][0]['indicators']['quote'][0]['open'],"high":stock['chart']['result'][0]['indicators']['quote'][0]['high'],"low":stock['chart']['result'][0]['indicators']['quote'][0]['low'],"volume":stock['chart']['result'][0]['indicators']['quote'][0]['volume']}


    for sList in sData:
        for stock in sList['spark']['result']:
            
            for i in range(len(stock['response'][0]['timestamp'])):
                a=datetime.now()
                if(datetime.fromtimestamp(stock['response'][0]['timestamp'][i]).day==a.day and datetime.fromtimestamp(stock['response'][0]['timestamp'][i]).month==a.month and datetime.fromtimestamp(stock['response'][0]['timestamp'][i]).year==a.year):
                    stock['response'][0]['timestamp']=stock['response'][0]['timestamp'][:-(len(stock['response'][0]['timestamp'])-i)]
                    stock['response'][0]['indicators']['quote'][0]['close']=stock['response'][0]['indicators']['quote'][0]['close'][:-(len(stock['response'][0]['indicators']['quote'][0]['close'])-i)]
                    break
            stock['response'][0]['timestamp']=stock['response'][0]['timestamp']+chartData[f"{stock['symbol']}"]['timestamp']#+chartTimestamp
            stock['response'][0]['indicators']['quote'][0]['close']=stock['response'][0]['indicators']['quote'][0]['close']+chartData[f"{stock['symbol']}"]['close']#+chartClose
            stData[f"{stock['symbol']}"]={"timestamp":stock['response'][0]['timestamp'],"close":stock['response'][0]['indicators']['quote'][0]['close']}
    with open('./website/json/stocksData/data30.json','w')as outfile:
        json.dump(stData,outfile)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    return stData
