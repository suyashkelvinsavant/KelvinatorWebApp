import requests,json

def screener():
    url = "https://query2.finance.yahoo.com/v1/finance/screener?crumb=if1GmG%2FbjeH"

    payload="{\"size\":200,\"offset\":0,\"sortField\":\"intradaymarketcap\",\"sortType\":\"DESC\",\"quoteType\":\"EQUITY\",\"topOperator\":\"AND\",\"query\":{\"operator\":\"AND\",\"operands\":[{\"operator\":\"or\",\"operands\":[{\"operator\":\"EQ\",\"operands\":[\"region\",\"in\"]}]},{\"operator\":\"or\",\"operands\":[{\"operator\":\"BTWN\",\"operands\":[\"intradaymarketcap\",10000000000,100000000000]},{\"operator\":\"GT\",\"operands\":[\"intradaymarketcap\",100000000000]}]},{\"operator\":\"gt\",\"operands\":[\"dayvolume\",1000000]},{\"operator\":\"btwn\",\"operands\":[\"intradayprice\",50,300]}]},\"userId\":\"\",\"userIdType\":\"guid\"}"
    headers = {
    'authority': 'query2.finance.yahoo.com',
    'cookie': 'B=b6r4avhfngecq&b=3&s=22; GUC=AQEBAgFgW4phIkIg-gTy; APID=1A6a2b265a-05a7-11eb-93f1-120f1417a350; A1=d=AQABBJo5eF8CEJc_jQ3m-tIWcJXXd_yKbLMFEgEBAgGKW2AiYVlQb2UB_eMAAAcImjl4X_yKbLM&S=AQAAAmxBPwoMKgEgn3XcBCzwE7o; A3=d=AQABBJo5eF8CEJc_jQ3m-tIWcJXXd_yKbLMFEgEBAgGKW2AiYVlQb2UB_eMAAAcImjl4X_yKbLM&S=AQAAAmxBPwoMKgEgn3XcBCzwE7o; PRF=t%3D%255ENSEI%252BITC.NS%252BBTC-USD%252BBTC%252BTATAMOTORS.NS; A1S=d=AQABBJo5eF8CEJc_jQ3m-tIWcJXXd_yKbLMFEgEBAgGKW2AiYVlQb2UB_eMAAAcImjl4X_yKbLM&S=AQAAAmxBPwoMKgEgn3XcBCzwE7o&j=WORLD; cmp=t=1619717557&j=0; APIDTS=1619717749; A1=d=AQABBMzEeF8CELswrEfGK4XX5mzoznUEUPoFEgEAAgJxM2AaYVlQb2UB_eMAAAcIzMR4X3UEUPoID_qGO_Os1W6IXvAiPRssQwkBAAoBvw&S=AQAAAgIKTonLOiayMm9xOeZMb74; A3=d=AQABBMzEeF8CELswrEfGK4XX5mzoznUEUPoFEgEAAgJxM2AaYVlQb2UB_eMAAAcIzMR4X3UEUPoID_qGO_Os1W6IXvAiPRssQwkBAAoBvw&S=AQAAAgIKTonLOiayMm9xOeZMb74; A1S=d=AQABBMzEeF8CELswrEfGK4XX5mzoznUEUPoFEgEAAgJxM2AaYVlQb2UB_eMAAAcIzMR4X3UEUPoID_qGO_Os1W6IXvAiPRssQwkBAAoBvw&S=AQAAAgIKTonLOiayMm9xOeZMb74&j=WORLD; B=fkk04elfnhh6c&b=4&d=B239rExtYFlEzrllOdgW&s=0p&i=.oY786zVbohe8CI9GyxD; GUC=AQEAAgJgM3FhGkIg2QSv',
    'Content-Type': 'text/plain'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    data=response.json()
    slist=[]
    for stockDetail in data["finance"]["result"][0]["quotes"]:
        if stockDetail['symbol'][-3:]==".NS":
            slist.append(stockDetail["symbol"]) 
    with open('./website/json/stockList/stockList.json','w')as outfile:
        json.dump(slist,outfile)