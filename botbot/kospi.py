from kindOfImport import *

def kospiFunc():
    kospiUrl= 'https://search.yahoo.com/search?p=kospi&fr=yfp-t&ei=UTF-8&fp=1'

    kospiHtml = urllib.request.urlopen(kospiUrl).read()
    kospiSoup = BeautifulSoup(kospiHtml, 'html.parser')

    
    kospiResponse = {
                "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            "simpleText": {
                                "text": "지수 : " + str(kospiSoup.select_one('.fin_quotePrice.s-price').get_text())
                            }
                        }
                    ]
                }
            }
    

    return kospiResponse

