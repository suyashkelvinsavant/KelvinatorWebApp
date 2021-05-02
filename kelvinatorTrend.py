import time,json,schedule,numbers
import numpy as np
from data5 import data5 
from data30 import data30 
from data60 import data60 
from analyse import analyse
from screener import screener
from datetime import datetime


while True:
    trendList=[]
    print("Downloading Data")
    dataFive=data5()
    dataThirty=data30()
    dataHour=data60()
    print("Downloading Complete")
    print("Analysing Data")
    indicator=analyse(dataFive,5)
    indicatorThirty=analyse(dataThirty,30)
    indicatorHour=analyse(dataHour,60)
    print("Analysing Complete")
    for symbol in indicatorHour:

            s=indicatorHour[symbol]
            p=indicatorThirty[symbol]
            d=indicator[symbol]
            i=len(s)-1
            j=len(p)-1
            k=len(d)-1
            hour=datetime.fromtimestamp((s[i][0]/1000)-19800).hour
            minute=datetime.fromtimestamp((s[i][0]/1000)-19800).minute
            hour1=s[i]
            if( hour1[3]>hour1[4]  and p[j][3]>p[j][4] and d[k][3]>d[k][4]):
                trendList.append(["BUY",symbol,d[k][1],f"{datetime.fromtimestamp((d[k][0]/1000)-19800)}"])              
            elif( hour1[3]<hour1[4] and p[j][3]>p[j][4] and d[k][3]>d[k][4]):
                trendList.append(["SELL",symbol,d[k][1],f"{datetime.fromtimestamp((d[k][0]/1000)-19800)}"])
    with open('./website/json/signal/trend.json','w')as outfile:
        json.dump(trendList,outfile)
    time.sleep(60)