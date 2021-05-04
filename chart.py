import grequests
import json
import time
from datetime import datetime

with open('./website/json/stockList/test.json') as f:
    stockList = json.load(f)
print(stockList)


# chartUrls=[]
# for symbol in stockList:
#     chartUrls.append(f"https://query1.finance.yahoo.com/v7/finance/chart/{symbol}?range=1d&interval=5m")
# crequest = (grequests.get(cu) for cu in chartUrls)
# cresult = grequests.map(crequest)
# cData = [cr.json() for cr in cresult]
# chartData={}
# for stock in cData:
#     chartData[f"{stock['chart']['result'][0]['meta']['symbol']}"]={"timestamp":stock['chart']['result'][0]['timestamp'],"close":stock['chart']['result'][0]['indicators']['quote'][0]['close'],"open":stock['chart']['result'][0]['indicators']['quote'][0]['open'],"high":stock['chart']['result'][0]['indicators']['quote'][0]['high'],"low":stock['chart']['result'][0]['indicators']['quote'][0]['low'],"volume":stock['chart']['result'][0]['indicators']['quote'][0]['volume']}
# with open('./website/json/stocksData/chart5.json','w')as outfile:
#     json.dump(chartData,outfile)