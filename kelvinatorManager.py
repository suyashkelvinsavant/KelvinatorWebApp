import time,requests,json
from datetime import datetime

marketStatusUrl = 'https://in.finance.yahoo.com/_finance_doubledown/api/resource/finance.market-time?bkt=finance-IN-en-IN-def&device=desktop&ecma=modern&feature=canvassOffnet%2CccOnMute%2CdisableCommentsMessage%2Cdebouncesearch100%2CdeferDarla%2CecmaModern%2CemptyServiceWorker%2CenableCCPAFooter%2CenableCMP%2CenableConsentData%2CenableGuceJs%2CenableGuceJsOverlay%2CenableNavFeatureCue%2CenablePrivacyUpdate%2CenableStreamDebounce%2CenableTheming%2CenableUpgradeLeafPage%2CenableVideoURL%2CenableYahooSans%2CenableYodleeErrorMsgCriOS%2CncpListStream%2CncpPortfolioStream%2CncpQspStream%2CncpStream%2CncpStreamIntl%2CncpTopicStream%2CnewContentAttribution%2CnewLogo%2CrelatedVideoFeature%2CvideoNativePlaylist%2CenhanceAddToWL&intl=in&lang=en-IN&partner=none&prid=4ju31mdfltmvl&region=IN&site=finance&tz=Asia%2FKolkata&ver=0.102.3964&returnMeta=true'
mStatusresponse=requests.get(url=marketStatusUrl)
mStatus=mStatusresponse.json()['data']['status']
profitRatio=0.02
lossRatio=0.01
while True:
    if mStatus=='open':
        while mStatus=='open':#True:#mStatus=='open':
            with open('./website/json/signal/tradeList.json') as f:
                tradeList = json.load(f)
            with open('./website/json/signal/tradeHistory.json') as h:
                tradeHistory=json.load(h)
                if(len(tradeList)>0):
                    symbolList=[]
                    #print(len(tradeList))
                    for l in range(0,len(tradeList)):
                        #print(l)
                        if(tradeList[l][7]=='Running'):
                            symbolList.append(tradeList[l][1])
                    s='%2C'
                    marketQuoteUrl=f'https://query1.finance.yahoo.com/v7/finance/quote?symbols={s.join(symbolList)}'
                    mQuoteresponse=requests.get(url=marketQuoteUrl)
                    dataList=mQuoteresponse.json()['quoteResponse']['result']
                    for i in range(len(dataList)):
                        for l in range(0,len(tradeList)-1):
                            symbol=dataList[i]['symbol']
                            currentPrice=dataList[i]['regularMarketPrice']
                            #print(symbol,currentPrice)
                            #print(l)
                            if(symbol==tradeList[l][1]):
                                hour=datetime.fromtimestamp(mQuoteresponse.json()['quoteResponse']['result'][0]['regularMarketTime']).hour
                                tradeList[l][4]=currentPrice
                                if(tradeList[l][0]=='Buy'):    
                                    tradeList[l][6]=((currentPrice-tradeList[l][2])/tradeList[l][2])*100
                                    if(currentPrice>=(tradeList[l][2]*0.02)+tradeList[l][2]):
                                        tradeList[l][7]='Buy Profit'
                                        tradeList[l][5]=currentPrice
                                        tradeHistory.append([tradeList[l][0],tradeList[l][1],tradeList[l][2],tradeList[l][3],tradeList[l][4],tradeList[l][5],tradeList[l][6],tradeList[l][7]])
                                        del tradeList[l]
                                    elif(currentPrice<=tradeList[l][2]-(tradeList[l][2]*0.01)):
                                        tradeList[l][7]='Buy Loss'
                                        tradeList[l][5]=currentPrice
                                        tradeHistory.append([tradeList[l][0],tradeList[l][1],tradeList[l][2],tradeList[l][3],tradeList[l][4],tradeList[l][5],tradeList[l][6],tradeList[l][7]])
                                        del tradeList[l]
                                    elif(hour==15):
                                        if(currentPrice>=tradeList[l][2]):
                                            tradeList[l][7]='Buy Profit'
                                            tradeList[l][5]=currentPrice
                                            tradeHistory.append([tradeList[l][0],tradeList[l][1],tradeList[l][2],tradeList[l][3],tradeList[l][4],tradeList[l][5],tradeList[l][6],tradeList[l][7]])
                                            del tradeList[l]
                                        elif(currentPrice<=tradeList[l][2]):
                                            tradeList[l][7]='Buy Loss'
                                            tradeList[l][5]=currentPrice
                                            tradeHistory.append([tradeList[l][0],tradeList[l][1],tradeList[l][2],tradeList[l][3],tradeList[l][4],tradeList[l][5],tradeList[l][6],tradeList[l][7]])
                                            del tradeList[l]
                                elif(tradeList[l][0]=='Sell'):
                                    tradeList[l][6]=((tradeList[l][2]-currentPrice)/tradeList[l][2])*100
                                    if(currentPrice<=tradeList[l][2]-(tradeList[l][2]*0.02)):
                                        tradeList[l][7]='Sell Profit'
                                        tradeList[l][5]=currentPrice
                                        tradeHistory.append([tradeList[l][0],tradeList[l][1],tradeList[l][2],tradeList[l][3],tradeList[l][4],tradeList[l][5],tradeList[l][6],tradeList[l][7]])
                                        del tradeList[l]
                                    elif(currentPrice>=(tradeList[l][2]*0.01)+tradeList[l][2]):
                                        tradeList[l][7]='Sell Loss'
                                        tradeList[l][5]=currentPrice
                                        tradeHistory.append([tradeList[l][0],tradeList[l][1],tradeList[l][2],tradeList[l][3],tradeList[l][4],tradeList[l][5],tradeList[l][6],tradeList[l][7]])
                                        del tradeList[l]
                                    elif(hour==15):
                                        if(currentPrice<=tradeList[l][2]):
                                            tradeList[l][7]='Sell Profit'
                                            tradeList[l][5]=currentPrice
                                            tradeHistory.append([tradeList[l][0],tradeList[l][1],tradeList[l][2],tradeList[l][3],tradeList[l][4],tradeList[l][5],tradeList[l][6],tradeList[l][7]])
                                            del tradeList[l]
                                        elif(currentPrice>=tradeList[l][2]):
                                            tradeList[l][7]='Sell Loss'
                                            tradeList[l][5]=currentPrice
                                            tradeHistory.append([tradeList[l][0],tradeList[l][1],tradeList[l][2],tradeList[l][3],tradeList[l][4],tradeList[l][5],tradeList[l][6],tradeList[l][7]])
                                            del tradeList[l]
                                continue
            with open('./website/json/signal/tradeList.json','w')as outfile:
                json.dump(tradeList,outfile)
            with open('./website/json/signal/tradeHistory.json','w')as of:
                json.dump(tradeHistory,of)
            mStatusresponse=requests.get(url=marketStatusUrl)
            mStatus=mStatusresponse.json()['data']['status']
            time.sleep(10)
    else:
        time.sleep(60)
