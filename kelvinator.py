from loadData import loadData
from loadThirtyData import loadThirtyData
from loadHourData import loadHourData
from analyse import analyse
import json
from datetime import datetime
import requests
import time
import schedule

while True:
    marketStatusUrl = 'https://in.finance.yahoo.com/_finance_doubledown/api/resource/finance.market-time?bkt=finance-IN-en-IN-def&device=desktop&ecma=modern&feature=canvassOffnet%2CccOnMute%2CdisableCommentsMessage%2Cdebouncesearch100%2CdeferDarla%2CecmaModern%2CemptyServiceWorker%2CenableCCPAFooter%2CenableCMP%2CenableConsentData%2CenableGuceJs%2CenableGuceJsOverlay%2CenableNavFeatureCue%2CenablePrivacyUpdate%2CenableStreamDebounce%2CenableTheming%2CenableUpgradeLeafPage%2CenableVideoURL%2CenableYahooSans%2CenableYodleeErrorMsgCriOS%2CncpListStream%2CncpPortfolioStream%2CncpQspStream%2CncpStream%2CncpStreamIntl%2CncpTopicStream%2CnewContentAttribution%2CnewLogo%2CrelatedVideoFeature%2CvideoNativePlaylist%2CenhanceAddToWL&intl=in&lang=en-IN&partner=none&prid=4ju31mdfltmvl&region=IN&site=finance&tz=Asia%2FKolkata&ver=0.102.3964&returnMeta=true'
    mStatusresponse=requests.get(url=marketStatusUrl)
    mStatus=mStatusresponse.json()['data']['status']
    #print(mStatus)
    if(mStatus=='open'):
        while mStatus=='open':#True:#mStatus=='open':
            data=loadData()
            dataThirty=loadThirtyData()
            dataHour=loadHourData()
            print('loaded Data')
            indicator=analyse(data,5)
            indicatorThirty=analyse(dataThirty,30)
            indicatorHour=analyse(dataHour,60)
            print('analysed Data')
            with open('./website/json/signal/tradeList.json') as f:
                tradeList = json.load(f)  
            for symbol in indicatorHour:
                s=indicatorHour[symbol]
                p=indicatorThirty[symbol]
                d=indicator[symbol]
                i=len(s)-1
                j=len(p)-1
                k=len(d)-1
                if(s[i-4][3]<s[i-4][4] and s[i-3][3]>s[i-3][4] and p[j][3]>p[j][4] and d[k][3]>d[k][4]):
                    tradeList.append(["Buy",symbol,d[k][1],f"{datetime.fromtimestamp((d[k][0]/1000)-19800)}",d[k][1],"-",0,"Running"])#{'x':d[k][0],'title':'Buy','text':d[k][1]})
                elif(s[i-4][3]>s[i-4][4] and s[i-3][3]<s[i-3][4] and p[j][3]<p[j][4] and d[k][3]<d[k][4]):    
                    tradeList.append(["Sell",symbol,d[k][1],f"{datetime.fromtimestamp((d[k][0]/1000)-19800)}",d[k][1],"-",0,"Running"])#{'x':d[k][0],'title':'Sell','text':d[k][1]})
            with open('./website/json/signal/tradeList.json','w')as outfile:
                json.dump(tradeList,outfile)
            time.sleep(3600)
            mStatusresponse=requests.get(url=marketStatusUrl)
            mStatus=mStatusresponse.json()['data']['status']
    else:
        time.sleep(60)

# from loadData import loadData
# from loadThirtyData import loadThirtyData
# from loadHourData import loadHourData
# from analyse import analyse
# import json
# from datetime import datetime
# import requests
# import time
# import schedule


# def kelvinator():
#     marketStatusUrl = 'https://in.finance.yahoo.com/_finance_doubledown/api/resource/finance.market-time?bkt=finance-IN-en-IN-def&device=desktop&ecma=modern&feature=canvassOffnet%2CccOnMute%2CdisableCommentsMessage%2Cdebouncesearch100%2CdeferDarla%2CecmaModern%2CemptyServiceWorker%2CenableCCPAFooter%2CenableCMP%2CenableConsentData%2CenableGuceJs%2CenableGuceJsOverlay%2CenableNavFeatureCue%2CenablePrivacyUpdate%2CenableStreamDebounce%2CenableTheming%2CenableUpgradeLeafPage%2CenableVideoURL%2CenableYahooSans%2CenableYodleeErrorMsgCriOS%2CncpListStream%2CncpPortfolioStream%2CncpQspStream%2CncpStream%2CncpStreamIntl%2CncpTopicStream%2CnewContentAttribution%2CnewLogo%2CrelatedVideoFeature%2CvideoNativePlaylist%2CenhanceAddToWL&intl=in&lang=en-IN&partner=none&prid=4ju31mdfltmvl&region=IN&site=finance&tz=Asia%2FKolkata&ver=0.102.3964&returnMeta=true'
#     mStatusresponse=requests.get(url=marketStatusUrl)
#     mStatus=mStatusresponse.json()['data']['status']
#     print(mStatus)
#     while mStatus=='open':
#         data=loadData()
#         dataThirty=loadThirtyData()
#         dataHour=loadHourData()
#         print('loaded Data')
#         indicator=analyse(data,5)
#         indicatorThirty=analyse(dataThirty,30)
#         indicatorHour=analyse(dataHour,60)
#         print('analysed Data')
#         with open('./json/signal/tradeList.json') as f:
#             tradeList = json.load(f)
#         for symbol in indicatorHour:
#             s=indicatorHour[symbol]
#             p=indicatorThirty[symbol]
#             d=indicator[symbol]
#             i=len(s)-1
#             j=len(p)-1
#             k=len(d)-1
#             hour=datetime.fromtimestamp((d[k][0]/1000)-19800).hour
#             if(len(tradeList)>0):
#                     for l in reversed(range(len(tradeList))):
#                         if(tradeList[l][6]=='Running'):
#                             tradeList[l][4]=d[k][1]
#                             marketQuoteUrl = f'https://query1.finance.yahoo.com/v7/finance/quote?symbols={tradeList[l][1]}'
#                             mQuoteresponse=requests.get(url=marketQuoteUrl)
#                             currentPrice=mQuoteresponse.json()['quoteResponse']['result'][0]['regularMarketPrice']
#                             if(tradeList[l][0]=='Buy'):    
#                                 tradeList[l][6]=((currentPrice-tradeList[l][2])/tradeList[l][2])*100
#                                 if(currentPrice>=(tradeList[l][2]*0.02)+tradeList[l][2]):
#                                     tradeList[l][7]='Buy Profit'
#                                     tradeList[l][5]=currentPrice
#                                 elif(currentPrice<=tradeList[l][2]-(tradeList[l][2]*0.01)):
#                                     tradeList[l][7]='Buy Loss'
#                                     tradeList[l][5]=currentPrice
#                                 elif(hour==15):
#                                     if(currentPrice>=tradeList[l][2]):
#                                         tradeList[l][7]='Buy Profit'
#                                         tradeList[l][5]=currentPrice
#                                     elif(currentPrice<=tradeList[l][2]):
#                                         tradeList[l][7]='Buy Loss'
#                                         tradeList[l][5]=currentPrice
#                             elif(tradeList[l][0]=='Sell'):
#                                 tradeList[l][6]=((tradeList[l][2]-currentPrice)/tradeList[l][2])*100
#                                 if(currentPrice<=tradeList[l][2]-(tradeList[l][2]*0.02)):
#                                     tradeList[l][7]='Sell Profit'
#                                     tradeList[l][5]=currentPrice
#                                 elif(currentPrice>=(tradeList[l][2]*0.01)+tradeList[l][2]):
#                                     tradeList[l][7]='Sell Loss'
#                                     tradeList[l][5]=currentPrice
#                                 elif(hour==15):
#                                     if(currentPrice<=tradeList[l][2]):
#                                         tradeList[l][7]='Sell Profit'
#                                         tradeList[l][5]=currentPrice
#                                     elif(currentPrice>=tradeList[l][2]):
#                                         tradeList[l][7]='Sell Loss'
#                                         tradeList[l][5]=currentPrice
#             if(s[i-1][3]<s[i-1][4] and s[i][3]>s[i][4] and p[j][3]>p[j][4] and d[k][3]>d[k][4]):
#                 tradeList.append(["Buy",symbol,d[k][1],f"{datetime.fromtimestamp((d[k][0]/1000)-19800)}",d[k][1],"-",0,"Running"])#{'x':d[k][0],'title':'Buy','text':d[k][1]})
#             elif(s[i-1][3]>s[i-1][4] and s[i][3]<s[i][4] and p[j][3]<p[j][4] and d[k][3]<d[k][4]):    
#                 tradeList.append(["Sell",symbol,d[k][1],f"{datetime.fromtimestamp((d[k][0]/1000)-19800)}",d[k][1],"-",0,"Running"])#{'x':d[k][0],'title':'Sell','text':d[k][1]})
#         with open('./json/signal/tradeList.json','w')as outfile:
#             json.dump(tradeList,outfile)
#         time.sleep(3600)
#         mStatusresponse=requests.get(url=marketStatusUrl)
#         mStatus=mStatusresponse.json()['data']['status']

# kelvinator()
#mQuoteUrl = f'https://query1.finance.yahoo.com/v7/finance/quote?symbols={symbols}'
#print(datetime.fromtimestamp((1616152500000/1000)-19800))
# def kelvinator():
#     marketStatusUrl = 'https://in.finance.yahoo.com/_finance_doubledown/api/resource/finance.market-time?bkt=finance-IN-en-IN-def&device=desktop&ecma=modern&feature=canvassOffnet%2CccOnMute%2CdisableCommentsMessage%2Cdebouncesearch100%2CdeferDarla%2CecmaModern%2CemptyServiceWorker%2CenableCCPAFooter%2CenableCMP%2CenableConsentData%2CenableGuceJs%2CenableGuceJsOverlay%2CenableNavFeatureCue%2CenablePrivacyUpdate%2CenableStreamDebounce%2CenableTheming%2CenableUpgradeLeafPage%2CenableVideoURL%2CenableYahooSans%2CenableYodleeErrorMsgCriOS%2CncpListStream%2CncpPortfolioStream%2CncpQspStream%2CncpStream%2CncpStreamIntl%2CncpTopicStream%2CnewContentAttribution%2CnewLogo%2CrelatedVideoFeature%2CvideoNativePlaylist%2CenhanceAddToWL&intl=in&lang=en-IN&partner=none&prid=4ju31mdfltmvl&region=IN&site=finance&tz=Asia%2FKolkata&ver=0.102.3964&returnMeta=true'
#     mStatusresponse=requests.get(url=marketStatusUrl)
#     mStatus=mStatusresponse.json()['data']['status']
#     print(mStatus)
#     while mStatus=='open':
#         data=loadData()
#         dataThirty=loadThirtyData()
#         dataHour=loadHourData()
#         indicator=analyse(data,5)
#         indicatorThirty=analyse(dataThirty,30)
#         indicatorHour=analyse(dataHour,60)

#         with open('./json/signal/tradeList.json') as f:
#             tradeList = json.load(f)
#         s=indicatorHour[symbol]
#         p=indicatorThirty[symbol]
#         d=indicator[symbol]
#         i=len(s)-1
#         j=len(p)-1
#         k=len(d)-1
#         hour=datetime.fromtimestamp((d[k][0]/1000)-19800).hour
#         if(len(tradeList)>0):
#                 for l in reversed(range(len(tradeList))):
#                     if(tradeList[l][6]=='Running'):
#                         tradeList[l][4]=d[k][1]
#                         if(tradeList[l][0]=='Buy'):
#                             tradeList[l][6]=((tradeList[l][2]-d[k][1])/d[k][1])*100
#                             if(d[k][1]>=(tradeList[l][2]*0.02)+tradeList[l][2]):
#                                 tradeList[l][7]='Buy Profit'
#                                 tradeList[l][5]=d[k][1]
#                             elif(d[k][1]<=tradeList[l][2]-(tradeList[l][2]*0.01)):
#                                 tradeList[l][7]='Buy Loss'
#                                 tradeList[l][5]=d[k][1]
#                             elif(hour==15):
#                                 if(d[k][1]>=tradeList[l][2]):
#                                     tradeList[l][7]='Buy Profit'
#                                     tradeList[l][5]=d[k][1]
#                                 elif(d[k][1]<=tradeList[l][2]):
#                                     tradeList[l][7]='Buy Loss'
#                                     tradeList[l][5]=d[k][1]
#                         elif(tradeList[l][0]=='Sell'):
#                             tradeList[l][6]=((d[k][1]-tradeList[l][2])/d[k][1])*100
#                             if(d[k][1]<=tradeList[l][2]-(tradeList[l][2]*0.02)):
#                                 tradeList[l][7]='Sell Profit'
#                                 tradeList[l][5]=d[k][1]
#                             elif(d[k][1]>=(tradeList[l][2]*0.01)+tradeList[l][2]):
#                                 tradeList[l][7]='Sell Loss'
#                                 tradeList[l][5]=d[k][1]
#                             elif(hour==15):
#                                 if(d[k][1]<=tradeList[l][2]):
#                                     tradeList[l][7]='Sell Profit'
#                                     tradeList[l][5]=d[k][1]
#                                 elif(d[k][1]>=tradeList[l][2]):
#                                     tradeList[l][7]='Sell Loss'
#                                     tradeList[l][5]=d[k][1]
#         for symbol in indicatorHour:
#             if(s[i-1][3]<s[i-1][4] and s[i][3]>s[i][4] and p[j][3]>p[j][4] and d[k][3]>d[k][4]):
#                 tradeList.append(["Buy",symbol,d[k][1],f"{datetime.fromtimestamp((d[k][0]/1000)-19800)}",d[k][1],"-",0,"Running"])#{'x':d[k][0],'title':'Buy','text':d[k][1]})
#             elif(s[i-1][3]>s[i-1][4] and s[i][3]<s[i][4] and p[j][3]<p[j][4] and d[k][3]<d[k][4]):    
#                 tradeList.append(["Sell",symbol,d[k][1],f"{datetime.fromtimestamp((d[k][0]/1000)-19800)}",d[k][1],"-",0,"Running"])#{'x':d[k][0],'title':'Sell','text':d[k][1]})
#         time.sleep(240)
#         mStatusresponse=requests.get(url=marketStatusUrl)
#         mStatus=mStatusresponse.json()['data']['status']


# schedule.every().monday.at("09:15:05").do(kelvinator)
# schedule.every().tuesday.at("09:15:05").do(kelvinator)
# schedule.every().wednesday.at("09:15:05").do(kelvinator)
# schedule.every().thursday.at("09:15:05").do(kelvinator)
# schedule.every().friday.at("09:15:05").do(kelvinator)

# while True:
#     schedule.run_pending()
#     time.sleep(1)
