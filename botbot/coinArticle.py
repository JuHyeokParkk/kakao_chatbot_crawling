from kindOfImport import *

def coinFunc():
    
    titles = []
    links = []
    images = []

    
    articleUrl = "https://m.search.naver.com/search.naver?where=m_news&sm=mtb_jum&query=비트코인" 
    usurl = 'https://coinmarketcap.com/currencies/bitcoin/'
    krurl = 'https://coinmarketcap.com/ko/currencies/bitcoin/'
    
    html = urllib.request.urlopen(krurl).read()
    soup = BeautifulSoup(html, 'html.parser')

    coin_price = soup.select_one('.priceValue___11gHJ').get_text()
    req = requests.get(articleUrl)
    articleHtml = req.text
    articleSoup = BeautifulSoup(articleHtml, 'html.parser')
    articleResult = articleSoup.select_one('#news_result_list')
    news_links = articleResult.select('.bx > .news_wrap > a ')
    image_links = articleResult.select('.bx > .news_wrap > .news_dsc img ')


    for image in image_links:
        images.append(image.attrs['src'])

    for title in news_links:
        titles.append(title.get_text())

    for link in news_links:
        links.append(link.attrs['href'])

    
   

    kimHtml = urllib.request.urlopen(usurl).read()
    kimSoup = BeautifulSoup(kimHtml, 'html.parser')

    usbit = kimSoup.select_one('.priceValue___11gHJ').get_text()

    kimHtml = urllib.request.urlopen(krurl).read()
    kimSoup = BeautifulSoup(kimHtml, 'html.parser')

    krbit = kimSoup.select_one('.priceValue___11gHJ').get_text()


    usbit = int(usbit[1]+usbit[2]+usbit[4]+usbit[5]+usbit[6]) * 1090
    krbit = int(krbit[1]+krbit[2]+krbit[4]+krbit[5]+krbit[6]+krbit[8]+krbit[9]+krbit[10])

    gap = (krbit-usbit) / usbit * 100
    gap = round(gap,2)

    coinResponse = {
              "version": "2.0", 
                "template": { 
                    "outputs": [
                   {
                "listCard": {
                  "header": {
                    "title": "현재 가격 : " + str(coin_price)
                  },
              "items": [
                {
                  "title": str(titles[0]),
                  "description": "첫 번째 뉴스",
                  "imageUrl": str(images[0]),
                  "link": {
                    "web": str(links[0])
                  }
                },
                {
                  "title": str(titles[1]),
                  "description":"두 번째 뉴스",
                  "imageUrl": str(images[1]),
                  "link": {
                    "web": str(links[1])
                   }
                },
                {
                  "title": str(titles[2]),
                  "description": "세 번째 뉴스",
                  "imageUrl": images[2],
                  "link": {
                    "web": str(links[2])
                  }
                }
              ],
    
              "buttons": [
                {
                  "label": "더 많은 뉴스 보러가기",
                  "action": "webLink",
                  "webLinkUrl": "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EB%B9%84%ED%8A%B8%EC%BD%94%EC%9D%B8"
                }
              ]
            }
          },
                        {
                            "simpleText": {
                                "text": "현재 국내 거래소에서의 비트코인은\n해외 거래소에서보다 약 " + str(gap) + "%\n비싸게 거래되고 있습니다." 
                            }
                        }
        ]
      }
     }
                    
                    
    
    return coinResponse

