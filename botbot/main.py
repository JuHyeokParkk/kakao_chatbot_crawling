from flask import Flask, request, jsonify
from dataLab import *
from coinArticle import *
from kindOfImport import *
from kospi import *
from nasdaq import *
from ticker import *
import os
import sys

app = Flask(__name__)
numberList = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']

kindOfSort = 0
startResponse = {
  "version": "2.0",
  "template": {
    "outputs": [
      {
        "basicCard": {
          "title": "트렌드 데이터 봇",
          "description": "하단의 카테고리에 관련된 정보들을\n확인해보세요!",
          "thumbnail": {
            "imageUrl": "https://ifh.cc/g/Ig2dYd.jpg"
          },
          "buttons": [
            {
              "action": "message",
              "label": "비트코인",
              "messageText": "비트코인"
            },
            {
              "action":  "message",
              "label": "주식",
              "messageText": "주식"
            },
              {
              "action":  "message",
              "label": "분야별 인기 검색어",
              "messageText": "분야별 인기 검색어"
            }
          ]
        }
      }
    ]
  }
}

testResponse = {
  "version": "2.0",
  "template": {
    "outputs": [
      {
        "carousel": {
          "type": "basicCard",
          "items": [
            {
              "title": "코스피",
              "description": "코스피 지수와 더 자세한 정보를 알아볼 수 있어요!",
              "thumbnail": {
                "imageUrl": "https://t1.daumcdn.net/cfile/tistory/993F22365F4A62312C"
              },
              "buttons": [
                {
                  "action": "message",
                  "label": "코스피 지수",
                  "messageText": "코스피"
                },
                {
                  "action":  "webLink",
                  "label": "더 알아보기",
                  "webLinkUrl": "https://www.google.com/finance/quote/KOSPI:KRX?sa=X&ved=2ahUKEwjIjvP4uKbxAhWsIqYKHdePD7wQ_AUoAXoECAEQAw"
                }
              ]
            },
            {
              "title": "나스닥",
              "description": "나스닥 지수와 더 자세한 정보를 알아볼 수 있어요!",
              "thumbnail": {
                "imageUrl": "https://blog.kakaocdn.net/dn/W3pu5/btqQgzdftUX/MiKmgaA7Y47lU7LXCPV1v0/img.jpg"
              },
              "buttons": [
                {
                  "action": "message",
                  "label": "나스닥 지수",
                  "messageText": "나스닥"
                },
                {
                  "action":  "webLink",
                  "label": "더 알아보기",
                  "webLinkUrl": "https://www.google.com/finance/quote/.IXIC:INDEXNASDAQ"
                }
              ]
            },
            {
              "title": "해외 주식",
              "description": "ticker 입력만으로 간편하게 가격 확인",
              "thumbnail": {
                "imageUrl": "https://apifriends.com/wp-content/uploads/2018/08/stock-market-ticker.jpg"
              },
              "buttons": [
                {
                  "action": "message",
                  "label": "Ticker 검색",
                  "messageText": "해외 주식"
                },
                {
                  "action":  "webLink",
                  "label": "시장 뉴스",
                  "webLinkUrl": "https://kr.investing.com/news/stock-market-news"
                }
              ]
            }
          ]
        }
      }
    ]
  }
}


@app.route('/message', methods=['POST'])
def coin():
    
    content = request.get_json()  # 사용자가 보낸 메세지 입력
    content = content['userRequest']
    content = content['utterance']
    
    print(content)
    
    global testResponse
    global kindOfSort
    global coinResponse
    global startResponse
    global dayResponse
    
    if content == u"처음으로":
        kindOfSort = 0
        return jsonify(startResponse)

    elif content == u"비트코인":
        return jsonify(coinFunc())

    elif content == u"주식":
        return jsonify(testResponse)

    elif content == u"코스피":
        return jsonify(kospiFunc())

    elif content == u"나스닥":
        return jsonify(nasdaqFunc())

    elif content == u"분야별 인기 검색어":
        return jsonify(dataNumber)

    elif content == u"해외 주식":
        response = {
                "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            "simpleText": {
                                "text": "해외 주식 티커(ticker)를 입력해주세요!"
                            }
                        }
                    ]
                }
         }

        return jsonify(response)

    elif content == u"개발자와의 소통":
        googleForm = {
          "version": "2.0",
          "template": {
            "outputs": [
              {
                "basicCard": {
                  "title": "개발자와의 소통",
                  "description": "궁금한 점을 물어보셔도 괜찮고,\n소통은 언제나 환영이에요!",
                 
                  "buttons": [
                    {
                      "action":  "webLink",
                      "label": "건의사항 문의하기",
                      "webLinkUrl": "https://docs.google.com/forms/d/e/1FAIpQLScPGSKPXVmxinFBNiXMxNuOG8OHvD72hu9XnL9I9oG9DxL-Wg/viewform?vc=0&c=0&w=1&flr=0"
                    }
                  ]
                }
              }
            ]
          }
        }

        return jsonify(googleForm)

    elif content in numberList:
        if kindOfSort == 0:
            kindOfSort = int(content)

            return jsonify(dayResponse)

        else:
            tempKindOfSort = kindOfSort
            kindOfSort = 0

            return jsonify(findCategory(tempKindOfSort,int(content)))

    else:
        return jsonify(tickerFunc(content))
   


if __name__=="__main__":
     app.run(host='0.0.0.0', port=80)

