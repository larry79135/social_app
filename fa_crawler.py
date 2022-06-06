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
options.add_argument("--disable-notifications"); 
chrome = webdriver.Chrome( chrome_options=options)
chrome.get("https://www.facebook.com/")
chrome.find_element_by_css_selector("#email").send_keys("larryshu.vistaxp@livemail.tw")

password=chrome.find_element_by_css_selector("#pass")
password.send_keys("pyla82465!")
password.submit()
time.sleep(2)
# chrome.get("https://www.facebook.com/hashtag/%E7%99%BE%E5%AE%B6%E6%A8%82")
chrome.get("https://www.facebook.com/hashtag/%E7%84%A1%E4%BA%BA%E6%A9%9F")
time.sleep(2)
moreList =chrome.find_elements_by_xpath("//*[text()='顯示更多']") 
for more in moreList:
    more.click()
    
contents =  chrome.find_elements_by_css_selector(".lzcic4wl[role=article]")
index = 1
article=1
for content in contents:
    top = content.find_element_by_class_name('ll8tlv6m')
    bottom = content.find_element_by_css_selector('.ecm0bbzt  .qzhwtbm6')
    
    author = top.find_element_by_css_selector('.nc684nl6 span')
    imgurl = top.find_element_by_css_selector('image').get_attribute('xlink:href')
    print("content",bottom.text)
    print("author:",author.text)
    # insert("facebook",bottom.text,author.text,imgurl)
    # print('author:'+author.text)
    # print('content:'+bottom.text)
    extra={
            "content":bottom.text,
            "author":author.text,
            "imgurl":imgurl,
        }
    LOGGER.info("Extra_fields",extra=extra)
    print('**********************************')
    # if index%2!=0:
    #     # print(contents[index].text)
    
    #     print('**********************************')
    #     article+=1
    
    print(f'第{index}篇')
    index+=1
    
# chrome.find_element_by_css_selector("#u_0_d_l1").click()

#email
# print(r.text)

#.q676j6op  image