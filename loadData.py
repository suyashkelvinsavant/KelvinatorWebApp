import grequests
import json
import time

def loadData():
    # with open('./json/stocksData/stocksData.json') as f:
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
        sUrls.append(f"https://query1.finance.yahoo.com/v7/finance/spark?symbols={s.join(slist)}&range=1mo&interval=5m")
    request = (grequests.get(u) for u in sUrls)
    result = grequests.map(request)
    sData = [r.json() for r in result]
    stData={}
    for sList in sData:
        for stock in sList['spark']['result']:
            stData[f"{stock['symbol']}"]={"marketPrice":stock['response'][0]['meta']['regularMarketPrice'],"timestamp":stock['response'][0]['timestamp'],"close":stock['response'][0]['indicators']['quote'][0]['close']}
    with open('./website/json/stocksData/stocksData.json','w')as outfile:
        json.dump(stData,outfile)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    return stData