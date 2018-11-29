
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

list_rank = 2

#데이터 수집
heart_count = driver.find_element_by_xpath("//em[@class = 'u_cnt _cnt']").text
reply_count = driver.find_element_by_xpath("//span[@class = 'count _commentCount']").text
play_count = driver.find_element_by_xpath("//span[@class = 'play']").text
is_he = he_name in driver.find_element_by_xpath("//h3[@class = '_clipTitle']").text
reply_list = []
replies = driver.find_elements_by_xpath("//span[@class = 'u_cbox_contents']")
for a in replies:
    reply_list.append(a.text)

#같은 회차 내 다음 영상으로 이동
click_path = "//*[@id='playlistClip']/li[{}]/div/dl/dt/a".format(list_rank)
click_element = driver.find_element_by_xpath(click_path)
click_element.click()
time.sleep(3)

#다음 재생목록으로 이동
click_path2 = //*[@id="playlistClipScrollBox"]/div[1]/div/div/ul/li[2]/a
click_element2 = driver.find_element_by_xpath(click_path2)
click_element2.click()
time.sleep(3)


# print(heart_count)
# print(reply_count)
# print(play_count)
# print(is_he)
# print(reply_list)
# print(playlisttitle)



