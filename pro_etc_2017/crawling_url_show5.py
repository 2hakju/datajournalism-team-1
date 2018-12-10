from bs4 import BeautifulSoup
import urllib.request

pro1 = 'balchick'
pro2 = 'voguemom'
pro3 = 'semobang'
pro4 = 'sectiontv'
pro5 = 'showmusic'
pro6 = 'ojimagic'


count = {'balch1': 659, 'balch2': 1852, 'balch3': 1079, 'balch4': 520,
        'vogue1': 0, 'vogue2': 0, 'vogue3': 852, 'vogue4': 1600,
        'semo1': 0, 'semo2': 961, 'semo3': 834, 'semo4': 508,
        'section1': 414, 'section2': 603, 'section3': 378, 'section4': 175,
        'show1': 96, 'show2': 118, 'show3': 79, 'show4': 64,
        'oji1': 0, 'oji2': 546, 'oji3': 396, 'oji4': 266}


str1 = 'https://search.naver.com/search.naver?&where=news&query={}'
#program name
md = '%EB%AC%B4%ED%95%9C%EB%8F%84%EC%A0%84'
bm = '%EB%B3%B5%EB%A9%B4%EA%B0%80%EC%99%95'
rs = '%EB%9D%BC%EB%94%94%EC%98%A4%EC%8A%A4%ED%83%80' 
mlt1 = '%EB%A7%88%EC%9D%B4%EB%A6%AC%ED%8B%80%ED%85%94%EB%A0%88%EB%B9%84%EC%A0%84'
mlt2 = '%EB%A7%88%EB%A6%AC%ED%85%94'

balch = '%EB%B0%9C%EC%B9%99%ED%95%9C%20%EB%8F%99%EA%B1%B0'
vogue = '%EB%B3%B4%EA%B7%B8%EB%A7%98'
semo = '%EC%84%B8%EB%AA%A8%EB%B0%A9'
section = '%EC%84%B9%EC%85%98tv'
show = '%EC%87%BC%EC%9D%8C%EC%95%85%EC%A4%91%EC%8B%AC'
oji = '%EC%98%A4%EC%A7%80%EC%9D%98%20%EB%A7%88%EB%B2%95%EC%82%AC'




str2 = '&sm=tab_pge&sort=2&photo=0&field=1&reporter_article=&pd=3&ds={}'



#quarter
quarter1 = ['2017.01.01&de=2017.03.31', '20170101to20170331']
quarter2 = ['2017.04.01&de=2017.06.30', '20170301to20170630']
quarter3 = ['2017.07.01&de=2017.09.30', '20170601to20170930']
quarter4 = ['2017.10.01&de=2017.12.28', '20171001to20171228']

str3 = '&docid=&nso=so:da,p:from{}'

str4 = ',a:t&mynews=0&start={}'

str5 = '&refresh_start=0'

urlfile = '{}2016_url{}.txt'

#'https://search.naver.com/search.naver?&where=news&query={}&sm=tab_pge&sort=2&photo=0&field=1&reporter_article=&pd=3&ds={}&docid=&nso=so:da,p:from{},a:t&mynews=0&start={}&refresh_start=0'




#4qt_show

url_list = []
for i in range(1, count['show4'], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(show, quarter4[0], quarter4[1], str(i))
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
f = open(urlfile.format(pro5, '4'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('4')

