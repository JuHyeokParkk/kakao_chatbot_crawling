from kindOfImport import *

def nasdaqFunc():
    nasdaqUrl= 'https://search.yahoo.com/search?p=nasdaq&fr=yfp-t&ei=UTF-8&fp=1'

    nasdaqHtml = urllib.request.urlopen(nasdaqUrl).read()
    nasdaqSoup = BeautifulSoup(nasdaqHtml, 'html.parser')


    nasdaqResponse = {
                "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            "simpleText": {
                                "text": "지수 : " + str(nasdaqSoup.select_one('.fin_quotePrice.s-price').get_text())
                            }
                        }
                    ]
                }
            }
    
    return nasdaqResponse