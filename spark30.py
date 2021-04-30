import grequests
import requests

import json
import time
from datetime import datetime

def spark30():
    # with open('./json/stocksData/stocksThirtyData.json') as f:
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
    for sList in sData:
        for stock in sList['spark']['result']:
            stockChartUrl = f"https://query1.finance.yahoo.com/v7/finance/chart/{stock['symbol']}?range=1d&interval=30m"
            stockChartResponse=requests.get(url=stockChartUrl)
            chartClose=stockChartResponse.json()['chart']['result'][0]['indicators']['quote'][0]['close']
            chartTimestamp=stockChartResponse.json()['chart']['result'][0]['timestamp']
            for i in range(len(stock['response'][0]['timestamp'])):
                a=datetime.now()
                if(datetime.fromtimestamp(stock['response'][0]['timestamp'][i]).day==a.day and datetime.fromtimestamp(stock['response'][0]['timestamp'][i]).month==a.month):
                    stock['response'][0]['timestamp']=stock['response'][0]['timestamp'][:-(len(stock['response'][0]['timestamp'])-i)]
                    stock['response'][0]['indicators']['quote'][0]['close']=stock['response'][0]['indicators']['quote'][0]['close'][:-(len(stock['response'][0]['indicators']['quote'][0]['close'])-i)]
                    break
            stock['response'][0]['timestamp']=stock['response'][0]['timestamp']+chartTimestamp
            stock['response'][0]['indicators']['quote'][0]['close']=stock['response'][0]['indicators']['quote'][0]['close']+chartClose
            stData[f"{stock['symbol']}"]={"timestamp":stock['response'][0]['timestamp'],"close":stock['response'][0]['indicators']['quote'][0]['close']}
    with open('./website/json/stocksData/spark30.json','w')as outfile:
        json.dump(stData,outfile)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    return stData