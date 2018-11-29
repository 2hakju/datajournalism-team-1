
from bs4 import BeautifulSoup
from selenium import webdriver
import time

data_list = []

#MBC 나혼자산다 2017년 1화 네이버 tv 링크
first_url = 'https://tv.naver.com/v/1356378/list/107821'
driver = webdriver.Chrome('C:\\Users\\bumso\\datajournalism-2018\\chromedriver_win32\\chromedriver.exe')
driver.get(first_url)
time.sleep(3)


# <span class="count _commentCount">30</span>
#<em class="u_cnt _cnt">334</em>
# tit_list = soup.find_all('div', class_ = 'tit_inner')("//div[@class='alex_more']")
heart_count = driver.find_element_by_xpath("//em[@class = 'u_cnt _cnt']").text
reply_count = driver.find_element_by_xpath("//span[@class = 'count _commentCount']").text


print(heart_count)
print(reply_count)