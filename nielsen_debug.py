
#%%
#url_list 만들기 
# --> 이부분 많이 수정했습니다! 

import datetime       

start_day = datetime.datetime(2017,1,1)   
one_day = datetime.timedelta(days = 1)    
end_day = datetime.datetime(2018,1,1)       

url_list = []
while start_day < end_day :
    dtdt = start_day.strftime("%Y%m%d")
    url_list.append("https://www.nielsenkorea.co.kr/tv_terrestrial_day.asp?menu=Tit_1&sub_menu=1_1&area=00&begin_date={}".format(dtdt))    
    start_day = start_day + one_day

#%%
#크롤링해서 JSON에 저장(문제는 중복된 프로그램명은 낮은 시청률을 반영한다는 것, 보수적 접근)
# pnss = OrderedDict()가 url_list 안을 도는 loop 밖에 있는 오류 수정했습니다. 

import urllib.request
from bs4 import BeautifulSoup
from collections import OrderedDict
import json

pn_list = []

for base_url in url_list:
    pnss = OrderedDict()
    with urllib.request.urlopen(base_url) as url:
    
        doc = url.read()
        soup = BeautifulSoup(doc, "html.parser")
        names = soup.find_all("td", class_="tb_txt")
        percents10 = soup.find_all("td", class_="percent")
        percents20 = soup.find_all("td", class_="percent_g")
    
        name_list = []
        percent_list = []
        pnss["날짜"] = base_url[-8:]
        for name in names[0:20]:
            name_list.append(name.text.strip())
        for percent10 in percents10[0:10]:
            percent_list.append(percent10.text.strip())
        for percent20 in percents20[0:10]:
            percent_list.append(percent20.text.strip())
        for i in range(0,20):
            pnss[name_list[i]] = percent_list[i]
        

    pn_list.append(pnss)
    
with open('rating2017.json', 'w', encoding="utf-8") as make_file:
    json.dump(pn_list, make_file, ensure_ascii=False, indent="\t")


#%%
url_list


