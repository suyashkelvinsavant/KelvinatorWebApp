import numpy as np
import tulipy as ti
import json


def analyse(data,timeframe):
    # with open('./json/indicator/indicator.json') as f:
    #     indicator = json.load(f)
    indicator={}
    for symbol in data:
        #print(symbol)
        close=data[symbol]['close'][:len(data[symbol]['close'])-2]
        timestamp=data[symbol]['timestamp'][:len(data[symbol]['timestamp'])-2]
        close60=close[::12]
        timestamp60=timestamp[::12]
        timestamp=[(timeStamp+19800)*1000 for timeStamp in timestamp]
        stockChart=list(zip(timestamp,close))
        npclose=np.array(close)
        nprsi=ti.rsi(npclose,9)
        rsi=[item.tolist() for item in np.round(nprsi,decimals=2)]
        rsiEma=[item.tolist() for item in np.round(ti.ema(nprsi,3),decimals=2)]
        ema=[item.tolist() for item in np.round(ti.ema(npclose,20),decimals=2)]
        wma=[item.tolist() for item in np.round(ti.wma(nprsi,21),decimals=2)]
        timestamp=timestamp[len(timestamp)-len(wma):]
        close=close[len(close)-len(wma):]
        rsiEma=rsiEma[len(rsiEma)-len(wma):]
        rsi=rsi[len(rsi)-len(wma):]
        ema=ema[len(ema)-len(wma):]
        tempIndicatorData=list(zip(timestamp,close,rsi,rsiEma,wma,ema))
        # with open(f'./website/json/indicator/{symbol}{timeframe}.json','w')as outfile:
        #     json.dump(tempIndicatorData,outfile)
        indicator[f"{symbol}"]=tempIndicatorData
    with open(f'./website/json/indicator/indicator{timeframe}.json','w')as outfile:
            json.dump(indicator,outfile)
    return indicator

# def analyse(data,timeframe):
#     # with open('./json/indicator/indicator.json') as f:
#     #     indicator = json.load(f)
#     indicator={}
#     for symbol in data:
# #        print(symbol)
#         close=data[symbol]['close']#[:len(data[symbol]['close'])-2]
#         timestamp=data[symbol]['timestamp']#[:len(data[symbol]['timestamp'])-2]
#         close60=close[::12]
#         timestamp60=timestamp[::12]
#         timestamp=[(timeStamp+19800)*1000 for timeStamp in timestamp]
#         stockChart=list(zip(timestamp,close))
#         npclose=np.array(close)
#         nprsi=ti.rsi(npclose,9)
#         rsi=[item.tolist() for item in np.round(nprsi,decimals=2)]
#         rsiEma=[item.tolist() for item in np.round(ti.ema(nprsi,3),decimals=2)]
#         ema=[item.tolist() for item in np.round(ti.ema(npclose,20),decimals=2)]
#         wma=[item.tolist() for item in np.round(ti.wma(nprsi,21),decimals=2)]
#         timestamp=timestamp[len(timestamp)-len(wma):]
#         close=close[len(close)-len(wma):]
#         rsiEma=rsiEma[len(rsiEma)-len(wma):]
#         rsi=rsi[len(rsi)-len(wma):]
#         ema=ema[len(ema)-len(wma):]
#         tempIndicatorData=list(zip(timestamp,close,rsi,rsiEma,wma,ema))
#         # with open(f'./website/json/indicator/{symbol}{timeframe}.json','w')as outfile:
#         #     json.dump(tempIndicatorData,outfile)
#         indicator[f"{symbol}"]=tempIndicatorData
#     with open(f'./website/json/indicator/indicator{timeframe}.json','w')as outfile:
#             json.dump(indicator,outfile)
#     return indicator
