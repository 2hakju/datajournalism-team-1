
from bs4 import BeautifulSoup
from selenium import webdriver
import time

data_list = []

#MBC 나혼자산다 2017년 1화 네이버 tv 링크
first_url = 'https://tv.naver.com/v/1356378/list/107821'
driver = webdriver.Chrome('C:\\Users\\bumso\\datajournalism-2018\\chromedriver_win32\\chromedriver.exe')
driver.get(first_url)
time.sleep(3)

he_name = "전현무"

# <span class="count _commentCount">30</span>
#<em class="u_cnt _cnt">334</em>
# tit_list = soup.find_all('div', class_ = 'tit_inner')("//div[@class='alex_more']")
heart_count = driver.find_element_by_xpath("//em[@class = 'u_cnt _cnt']").text
reply_count = driver.find_element_by_xpath("//span[@class = 'count _commentCount']").text
play_count = driver.find_element_by_xpath("//span[@class = 'play']").text
is_he = he_name in driver.find_element_by_xpath("//h3[@class = '_clipTitle']").text
reply_list = []
replies = driver.find_elements_by_xpath("//span[@class = 'u_cbox_contents']")
for a in replies:
    reply_list.append(a.text)
playlisttitle = driver.find_element_by_xpath("//span[@class = '_playlistTitle']").text

print(heart_count)
print(reply_count)
print(play_count)
print(is_he)
print(reply_list)
print(playlisttitle)



