#%%
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from datetime import datetime
import json

first_url = 'https://tv.naver.com/v/1356378/list/107821'
driver = webdriver.Chrome('C:\\Users\\bumso\\datajournalism-2018\\chromedriver_win32\\chromedriver.exe')
driver.get(first_url)
time.sleep(3)
click_path = "//*[@id='playlistClip']/li[8]/div/dl/dt/a"
click_element = driver.find_element_by_xpath(click_path)
click_element.click()
time.sleep(3)
click_path3 = "//*[@id='playlistClip']/li[14]/div/dl/dt/a"
click_element3 = driver.find_element_by_xpath(click_path3)
click_element3.click()
time.sleep(3)
click_path2 = '//*[@id="playlistClipScrollBox"]/div[1]/div/div/ul/li[2]/a/div/strong'
click_element2 = driver.find_element_by_xpath(click_path2)
click_element2.click()