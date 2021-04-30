import grequests
import json
import time


def chart60():
    # with open('./website/json/stocksData/data60.json') as f:
    #     stData = json.load(f)
    with open('./website/json/stockList/stockList.json') as f:
        stockList = json.load(f)
    sUrls=[]
    for symbol in stockList:
        sUrls.append(f"https://query1.finance.yahoo.com/v7/finance/chart/{symbol}?range=1d&interval=1h")
    request = (grequests.get(u) for u in sUrls)
    result = grequests.map(request)
    sData = [r.json() for r in result]
    stData={}
    for stock in sData:
       stData[f"{stock['chart']['result'][0]['meta']['symbol']}"]={"timestamp":stock['chart']['result'][0]['timestamp'],"close":stock['chart']['result'][0]['indicators']['quote'][0]['close'],"open":stock['chart']['result'][0]['indicators']['quote'][0]['open'],"high":stock['chart']['result'][0]['indicators']['quote'][0]['high'],"low":stock['chart']['result'][0]['indicators']['quote'][0]['low'],"volume":stock['chart']['result'][0]['indicators']['quote'][0]['volume']}
    with open('./website/json/stocksData/chart60.json','w')as outfile:
        json.dump(stData,outfile)
    return stData
