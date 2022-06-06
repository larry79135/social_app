from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from mysql import insert
options = Options()
options.add_argument("--disable-notifications")
chrome = webdriver.Chrome( chrome_options=options)

# chrome.get("https://www.dcard.tw/topics/%E7%99%BE%E5%AE%B6%E6%A8%82")
chrome.get("https://www.dcard.tw/topics/iphone")
article_list=chrome.find_elements_by_css_selector("#__next > div.bvk29r-0.eFPEdc > div.bvk29r-2.etVvYS > div > div > div > div > div.sc-1wisey8-0.dRDKvl > div > div > div:nth-child(1) > div")
article_num=1
for article in article_list:
    time.sleep(2)
    article.click()
    time.sleep(2)
    #author
    author=chrome.find_element_by_css_selector("body > div.__portal > div > div.pup2eh-0.edtyEf > div.sc-qz0f8b.dCgfWN.simplebar-scrollable-y > div.simplebar-wrapper > div.simplebar-mask > div > div > div > div > div > div.sc-1oj78p7-0.gjnISi").text
    print("author:",author)
    #title
    # title=chrome.find_element_by_css_selector("body > div.__portal > div > div.pup2eh-0.edtyEf > div.sc-qz0f8b.dCgfWN.simplebar-scrollable-y > div.simplebar-wrapper > div.simplebar-mask > div > div > div > div > div > article > div.sc-1eorkjw-1.ccTaOU > div > h1").text
    # print("title:",title)
    #content
    content=chrome.find_element_by_css_selector("body > div.__portal > div > div.pup2eh-0.edtyEf > div.sc-qz0f8b.dCgfWN.simplebar-scrollable-y > div.simplebar-wrapper > div.simplebar-mask > div > div > div > div > div > article").text
    print("content:",content)
    # insert("dcard",content,author,'')
    print(f'第{article_num}篇')
    article_num+=1
    time.sleep(2)
    #關掉
    chrome.find_element_by_css_selector("body > div.__portal > div > div.pup2eh-0.edtyEf > div.sc-qz0f8b.dCgfWN.simplebar-scrollable-y > div.simplebar-wrapper > div.simplebar-mask > div > div > div > div > div > div.sc-1oj78p7-0.gjnISi > button").click()