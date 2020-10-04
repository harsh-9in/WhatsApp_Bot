from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

chrome=webdriver.Chrome(ChromeDriverManager().install())
time.sleep(3)


chrome.get("https://web.whatsapp.com/")
time.sleep(10)

search_box = chrome.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
name= input()
search_box.send_keys(name)
search_box.send_keys(Keys.ENTER)

message_box=chrome.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
for i in range(0,20):
    message_box.send_keys("happy")
    message_box.send_keys(Keys.ENTER)
    time.sleep(1)
