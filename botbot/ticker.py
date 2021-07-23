from kindOfImport import *

def tickerFunc(tickerName):
    tickerName = tickerName.lower()
    
    try:
        tickerUrl= 'https://www.webull.com/quote/nasdaq-' + tickerName

        tickerHtml = urllib.request.urlopen(tickerUrl).read()
        tickerSoup = BeautifulSoup(tickerHtml, 'html.parser')
        
        answer =""

        if tickerSoup.select_one('.jss13nkew4.jss1av2zhw') != None :
            answer = tickerSoup.select_one('.jss13nkew4.jss1av2zhw').get_text()

            
        elif tickerSoup.select_one('.jssazadn6.jss1av2zhw') != None :
            answer = tickerSoup.select_one('.jssazadn6.jss1av2zhw').get_text()


        else :
            tickerUrl= 'https://www.webull.com/quote/nyse-' + tickerName
            tickerHtml = urllib.request.urlopen(tickerUrl).read()
            tickerSoup = BeautifulSoup(tickerHtml, 'html.parser')
        
        if tickerSoup.select_one('.jss13nkew4.jss1av2zhw') != None:
            answer = tickerSoup.select_one('.jss13nkew4.jss1av2zhw').get_text()

        elif tickerSoup.select_one('.jssazadn6.jss1av2zhw') != None:
            answer = tickerSoup.select_one('.jssazadn6.jss1av2zhw').get_text()
            
        else :
            tickerUrl= 'https://www.webull.com/quote/amex-' + tickerName
            tickerHtml = urllib.request.urlopen(tickerUrl).read()
            tickerSoup = BeautifulSoup(tickerHtml, 'html.parser')
    
        if tickerSoup.select_one('.jss13nkew4.jss1av2zhw') != None:
            answer = tickerSoup.select_one('.jss13nkew4.jss1av2zhw').get_text()

        elif tickerSoup.select_one('.jssazadn6.jss1av2zhw') != None:
            answer = tickerSoup.select_one('.jssazadn6.jss1av2zhw').get_text()
            
        else:
            answer = tickerSoup.select_one('.jssazadn6.jss1av2zhw').get_text()

    except:
        print("except실행")
        failResponse = {
    "version": "2.0",
    "template": {"outputs": [{"simpleText": {"text": "잘못 입력하셨습니다. 다시 선택해주세요!"}}],
                 "quickReplies": [
                                  {"label": "건의사항 문의", "action": "message", "messageText": "건의사항 문의"},
                                  {"label": "분야별 인기 검색어", "action": "message", "messageText": "분야별 인기 검색어"},
                                  {"label": "주식", "action": "message", "messageText": "주식"},
                                  {"label": "비트코인", "action": "message", "messageText": "비트코인"},
                                  {"label": "처음으로", "action": "message", "messageText": "처음으로"}
                                  
                                  ]
                 }
}
        
        return failResponse
    
    else:
        print("실행성공")
        tickerResponse = {
                "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            "simpleText": {
                                "text": str(tickerName) + "의 현재 가격은 : " + str(answer) +"$ 입니다."
                            }
                        }
                    ]
                }
            }
        
        return tickerResponse