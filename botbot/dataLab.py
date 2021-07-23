from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from kindOfImport import *
import time
import datetime

now = datetime.date.today()
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument('disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
options.add_argument('--ignore-certificate-errors')


driver = webdriver.Chrome(options=options)
driver.get("https://datalab.naver.com/")
driver.find_element_by_xpath('//div[@data-default-cid]').click()

options.add_argument('disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
options.add_argument('--ignore-certificate-errors')

dataNumber = {
    "version": "2.0",
    "template": {"outputs": [{"simpleText": {"text": "알고 싶은 카테고리를 눌러주세요!"}}],
                 "quickReplies": [{"label": "패션의류", "action": "message", "messageText": "1"},
                                  {"label": "패션잡화", "action": "message", "messageText": "2"},
                                  {"label": "화장품/미용", "action": "message", "messageText": "3"},
                                  {"label": "디지털/가전", "action": "message", "messageText": "4"},
                                  {"label": "가구/인테리어", "action": "message", "messageText": "5"},
                                  {"label": "출산/육아", "action": "message", "messageText": "6"},
                                  {"label": "식품", "action": "message", "messageText": "7"},
                                  {"label": "스포츠/레저", "action": "message", "messageText": "8"},
                                  {"label": "생활/건강", "action": "message", "messageText": "9"},
                                  {"label": "여가/생활편의", "action": "message", "messageText": "10"},
                                  {"label": "면세점", "action": "message", "messageText": "11"}
                                  ]
                 }
}

dayResponse = {
                "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            "simpleText": {
                                "text": "며칠 전 인기 검색어 순위가 궁금하신가요?(1~12 이내의 숫자 입력)"
                            }
                        }
                    ]
                }
            }

def findCategory(category, day):
    
    global driver
    global now
    
    time.sleep(1)
    
    dataCid = str('//li/a[@data-cid="500000')
    if category == 11:
        dataCid = dataCid + "10"
    else:
        dataCid = dataCid + "0" + str(category)    
    dataCid = dataCid + '"' + "]"
    
    driver.find_element_by_xpath(dataCid).click()
    
        
    dataHtml = driver.page_source
    dataSoup = BeautifulSoup(dataHtml, 'html.parser')
    
    a = dataSoup.select('.title')
    
    
    dataAnswer = "[" + str(now) + "]" + "일 기준\n" + str(day) + "일 전의 인기 검색어 순위\n\n"
    dataAnswer = dataAnswer + "=====================\n"
    
    for i in range (1,11):
        dataAnswer = dataAnswer + str(i) + "위 : " + str(a[120 - 10*day + i].get_text()) + "\n"
    
    dataAnswer = dataAnswer + "====================="
    dataResponse = {
                "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            "simpleText": {
                                "text": str(dataAnswer)
                            }
                        }
                    ]
                }
            }
    
   
    driver.get("https://datalab.naver.com/")
    driver.find_element_by_xpath('//div[@data-default-cid]').click()
    

    return dataResponse
    
        
