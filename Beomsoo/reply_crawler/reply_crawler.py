#%%
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from datetime import datetime
import json
from collections import OrderedDict
import urllib.request

#리스트내에서 이동하기! 

with open(r'C:\Users\bumso\datajournalism-2018\datajournalism-team-1\Beomsoo\reply_crawler\urls\2017\bokmyengawang_url4.txt', 'r', encoding = 'utf-8') as file:
        bokga2017_4 = file.readlines()

for 
reply_list  = []
driver = webdriver.Chrome('C:\\Users\\bumso\\datajournalism-2018\\chromedriver_win32\\chromedriver.exe')
order = 1
for u in bokga2017_4: 
        driver.get(u)
        time.sleep(2)
        replies = driver.find_elements_by_xpath("//span[@class = 'u_cbox_contents']") 
        for a in replies:
                reply_list.append(a.text)
                print(a.text)
        print("{} / {}".format(order, len(bokga2017_4)))
        order += 1


