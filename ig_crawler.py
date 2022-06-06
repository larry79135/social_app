from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from mysql import insert
import logging
import logstash


LOGGER = logging.getLogger('python-logstash-logger') 
LOGGER.setLevel(logging.INFO) 
LOGGER.addHandler (logstash.TCPLogstashHandler("127.0.0.1", "5000", version=1)) 
LOGGER.error('python-logstash: test logstash error message.')

options = Options()
options.add_argument("--disable-notifications")
chrome = webdriver.Chrome( chrome_options=options)
chrome.get("https://www.instagram.com/")
time.sleep(1)
chrome.find_element_by_css_selector("#loginForm > div > div:nth-child(1) > div > label > input").send_keys("larrygbm1@gmail.com")
#loginForm > div > div:nth-child(1) > div > label > input
password=chrome.find_element_by_css_selector("#loginForm > div > div:nth-child(2) > div > label > input").send_keys("larry79135")

chrome.find_element_by_css_selector("#loginForm > div > div:nth-child(3) > button").click()
# chrome.find_element_by_css_selector("#react-root > section > main > div > div > div > div > button").click()
time.sleep(3)

# chrome.get("https://www.instagram.com/explore/tags/%E7%99%BE%E5%AE%B6%E6%A8%82/")
chrome.get("https://www.instagram.com/explore/tags/%E7%84%A1%E4%BA%BA%E6%A9%9F/")
time.sleep(3)
articles=chrome.find_elements_by_class_name("Nnq7C")
article_num=1
for article in articles:
    small_articles=article.find_elements_by_class_name("v1Nh3")
    for small_article in small_articles:
        small_article.click()
        time.sleep(3)
        author =chrome.find_element_by_css_selector('header .o-MQd a').text
        imgurl =chrome.find_element_by_css_selector('header ._2dbep img').get_attribute('src')

        text=chrome.find_element_by_css_selector("body > div.RnEpo._Yhr4 > div.pbNvD.QZZGH.bW6vo > div > article > div > div.HP0qD > div > div > div.eo2As > div.EtaWk > ul > div > li > div > div > div.C4VMK").text
        insert("instagram",text,author,imgurl)
        print("content:",text)
        
        print("author:",author)
        print("imgurl:",imgurl)
        # extra={
        #     "content":text,
        #     "author":author,
        #     "imgurl":imgurl,
        # }
        print(f'第{article_num}篇')
        # LOGGER.info("Extra_fields",extra=extra)
        article_num+=1
        
        #關掉
        chrome.find_element_by_css_selector("body > div.RnEpo._Yhr4 > div.NOTWr > button").click()
        # print(article)
