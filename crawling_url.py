from bs4 import BeautifulSoup
import urllib.request
from urllib import parse

pro = 'mylttletv2' #이 부분을 바꾸세요
#count = [256, 180, 109, 125, 114, 78, 110, 30, 87, 103, 84, 70]
count = [2771, 1669, 971, 1108, 715, 500, 619, 139, 620, 356, 280, 182] #이 부분을 바꾸세요 (기사 수입니다. for루프 돌릴 때 필요해요.)

str1 = 'https://search.naver.com/search.naver?&where=news&query={}'

#program name (이 부분은 from urllib import parse로 바꿔 써도 무방할 것 같습니다.)
'''
md = '%EB%AC%B4%ED%95%9C%EB%8F%84%EC%A0%84'
bm = '%EB%B3%B5%EB%A9%B4%EA%B0%80%EC%99%95'
rs = '%EB%9D%BC%EB%94%94%EC%98%A4%EC%8A%A4%ED%83%80' 
mlt1 = '%EB%A7%88%EC%9D%B4%EB%A6%AC%ED%8B%80%ED%85%94%EB%A0%88%EB%B9%84%EC%A0%84'
mlt2 = '%EB%A7%88%EB%A6%AC%ED%85%94'
'''
md = parse.quote('무한도전')
bm = parse.quote('복면가왕')
rs = parse.quote('라디오스타') 
mlt1 = parse.quote('마이리틀텔레비전')
mlt2 = parse.quote('마리텔')

weirdnm = mlt2 #이 부분은 검색 내용 설정한 것입니다.

str2 = '&sm=tab_pge&sort=2&photo=0&field=1&reporter_article=&pd=3&ds={}'

#day #이 부분은 날짜입니다. 2017년으로 바꿔서 사용하면 됩니다. 
january = '2016.01.01&de=2016.01.31'
february = '2016.02.01&de=2016.02.28'
march = '2016.03.01&de=2016.03.31'
april = '2016.04.01&de=2016.04.30'
may = '2016.05.01&de=2016.05.31'
june = '2016.06.01&de=2016.06.30'
july = '2016.07.01&de=2016.07.31'
august = '2016.08.01&de=2016.08.31'
september = '2016.09.01&de=2016.09.30'
october = '2016.10.01&de=2016.10.31'
november = '2016.11.01&de=2016.11.31'
december = '2016.12.01&de=2016.12.28'

str3 = '&docid=&nso=so:da,p:from{}'

#day #이 부분도 날짜입니다. 위와 일치해야 합니다. 
month1 = '20160101to20160131'
month2 = '20160201to20160228'
month3 = '20160301to20160331'
month4 = '20160401to20160430'
month5 = '20160501to20160531'
month6 = '20160601to20160630'
month7 = '20160701to20160731'
month8 = '20160801to20160831'
month9 = '20160901to20160330'
month10 = '20161001to20161031'
month11 = '20161101to20161130'
month12 = '20161201to20161228'

str4 = ',a:t&mynews=0&start={}'

str5 = '&refresh_start=0'

#최종 생성되는 파일 이름입니다. 
urlfile = '{}2016_url{}.txt'


#기사수가 너무 많아 월별로 뽑았으나 2017년은 분기별로 뽑아도 될 것 같습니다. 

#1월

url_list = []
for i in range(1, count[0], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(weirdnm, january, month1, str(i))
    url_list.append(strurl)
    
news_url = []    
for urls in url_list:
    with urllib.request.urlopen(urls) as url:
        doc = url.read()
        soup = BeautifulSoup(doc, "html.parser")
        dds = soup.find_all("dd", class_="txt_inline")
        for dd in dds:
            if len(dd.a["href"]) > 10:
                news_url.append(dd.a["href"])
            else:
                pass
f = open(urlfile.format(pro, '1'), 'w', encoding='utf-8')
for i in news_url:
    data = i + ''
    f.write(data)
f.close()
print('1')


#2
url_list = []
for i in range(1, count[1], 10):  #this can be changed (0 - 1705, 1343, 1361, 2269, 676)
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(weirdnm, february, month2, str(i))
    url_list.append(strurl)

news_url = []    
for urls in url_list:
    with urllib.request.urlopen(urls) as url:
        doc = url.read()
        soup = BeautifulSoup(doc, "html.parser")
        dds = soup.find_all("dd", class_="txt_inline")
        for dd in dds:
            if len(dd.a["href"]) > 10:
                news_url.append(dd.a["href"])
            else:
                pass
with open(urlfile.format(pro, '2'), 'w', encoding='utf-8') as f:
    for i in news_url:
        data = i + '\n'
        f.write(data)

print('2')


#3
url_list = []
for i in range(1, count[2], 10):  #this can be changed (0 - 1705, 1343, 1361, 2269, 676)
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(weirdnm, march, month3, str(i))
    url_list.append(strurl)

news_url = []    
for urls in url_list:
    with urllib.request.urlopen(urls) as url:
        doc = url.read()
        soup = BeautifulSoup(doc, "html.parser")
        dds = soup.find_all("dd", class_="txt_inline")
        for dd in dds:
            if len(dd.a["href"]) > 10:
                news_url.append(dd.a["href"])
            else:
                pass
with open(urlfile.format(pro, '3'), 'w', encoding='utf-8') as f:
    for i in news_url:
        data = i + '\n'
        f.write(data)

print('3')


#4
url_list = []
for i in range(1, count[3], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(weirdnm, april, month4, str(i))
    url_list.append(strurl)

news_url = []    
for urls in url_list:
    with urllib.request.urlopen(urls) as url:
        doc = url.read()
        soup = BeautifulSoup(doc, "html.parser")
        dds = soup.find_all("dd", class_="txt_inline")
        for dd in dds:
            if len(dd.a["href"]) > 10:
                news_url.append(dd.a["href"])
            else:
                pass
f = open(urlfile.format(pro, '4'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('4')

#5
url_list = []
for i in range(1, count[4], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(weirdnm, may, month5, str(i))
    url_list.append(strurl)

    
news_url = []    
for urls in url_list:
    with urllib.request.urlopen(urls) as url:
        doc = url.read()
        soup = BeautifulSoup(doc, "html.parser")
        dds = soup.find_all("dd", class_="txt_inline")
        for dd in dds:
            if len(dd.a["href"]) > 10:
                news_url.append(dd.a["href"])
            else:
                pass
f = open(urlfile.format(pro, '5'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('5')

#6
url_list = []
for i in range(1, count[5], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(weirdnm, june, month6, str(i))
    url_list.append(strurl)

    
news_url = []    
for urls in url_list:
    with urllib.request.urlopen(urls) as url:
        doc = url.read()
        soup = BeautifulSoup(doc, "html.parser")
        dds = soup.find_all("dd", class_="txt_inline")
        for dd in dds:
            if len(dd.a["href"]) > 10:
                news_url.append(dd.a["href"])
            else:
                pass
f = open(urlfile.format(pro, '6'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('6')


#7
url_list = []
for i in range(1, count[6], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(weirdnm, july, month7, str(i))
    url_list.append(strurl)

    
news_url = []    
for urls in url_list:
    with urllib.request.urlopen(urls) as url:
        doc = url.read()
        soup = BeautifulSoup(doc, "html.parser")
        dds = soup.find_all("dd", class_="txt_inline")
        for dd in dds:
            if len(dd.a["href"]) > 10:
                news_url.append(dd.a["href"])
            else:
                pass
f = open(urlfile.format(pro, '7'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('7')

#8
url_list = []
for i in range(1, count[7], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(weirdnm, august, month8, str(i))
    url_list.append(strurl)

    
news_url = []    
for urls in url_list:
    with urllib.request.urlopen(urls) as url:
        doc = url.read()
        soup = BeautifulSoup(doc, "html.parser")
        dds = soup.find_all("dd", class_="txt_inline")
        for dd in dds:
            if len(dd.a["href"]) > 10:
                news_url.append(dd.a["href"])
            else:
                pass
f = open(urlfile.format(pro, '8'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('8')

#9
url_list = []
for i in range(1, count[8], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(weirdnm, september, month9, str(i))
    url_list.append(strurl)

    
news_url = []    
for urls in url_list:
    with urllib.request.urlopen(urls) as url:
        doc = url.read()
        soup = BeautifulSoup(doc, "html.parser")
        dds = soup.find_all("dd", class_="txt_inline")
        for dd in dds:
            if len(dd.a["href"]) > 10:
                news_url.append(dd.a["href"])
            else:
                pass
f = open(urlfile.format(pro, '9'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('9')

#10
url_list = []
for i in range(1, count[9], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(weirdnm, october, month10, str(i))
    url_list.append(strurl)

    
news_url = []    
for urls in url_list:
    with urllib.request.urlopen(urls) as url:
        doc = url.read()
        soup = BeautifulSoup(doc, "html.parser")
        dds = soup.find_all("dd", class_="txt_inline")
        for dd in dds:
            if len(dd.a["href"]) > 10:
                news_url.append(dd.a["href"])
            else:
                pass
f = open(urlfile.format(pro, '10'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('10')

#11
url_list = []
for i in range(1, count[10], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(weirdnm, november, month11, str(i))
    url_list.append(strurl)

    
news_url = []    
for urls in url_list:
    with urllib.request.urlopen(urls) as url:
        doc = url.read()
        soup = BeautifulSoup(doc, "html.parser")
        dds = soup.find_all("dd", class_="txt_inline")
        for dd in dds:
            if len(dd.a["href"]) > 10:
                news_url.append(dd.a["href"])
            else:
                pass
f = open(urlfile.format(pro, '11'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('11')

#12
url_list = []
for i in range(1, count[11], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(weirdnm, december, month12, str(i))
    url_list.append(strurl)
    
news_url = []    
for urls in url_list:
    with urllib.request.urlopen(urls) as url:
        doc = url.read()
        soup = BeautifulSoup(doc, "html.parser")
        dds = soup.find_all("dd", class_="txt_inline")
        for dd in dds:
            if len(dd.a["href"]) > 10:
                news_url.append(dd.a["href"])
            else:
                pass
f = open(urlfile.format(pro, '12'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('12')