from bs4 import BeautifulSoup
import urllib.request


#1
url_list = []

str1 = "https://search.naver.com/search.naver?&where=news&query=%EB%B3%B5%EB%A9%B4%EA%B0%80%EC%99%95&sm=tab_pge&sort=2&photo=0&field=1&reporter_article=&pd=3&ds=2017.01.01&de=2017.03.31&docid=&nso=so:da,p:from20170101to20170331,a:t&mynews=0&start="
#str1 = "https://search.naver.com/search.naver?&where=news&query=%EB%B3%B5%EB%A9%B4%EA%B0%80%EC%99%95&sm=tab_pge&sort=2&photo=0&field=1&reporter_article=&pd=3&ds=2017.04.01&de=2017.06.30&docid=&nso=so:da,p:from20170401to20170630,a:t&mynews=0&start="
#str1 = "https://search.naver.com/search.naver?&where=news&query=%EB%B3%B5%EB%A9%B4%EA%B0%80%EC%99%95&sm=tab_pge&sort=2&photo=0&field=1&reporter_article=&pd=3&ds=2017.07.01&de=2017.09.30&docid=&nso=so:da,p:from20170701to20170930,a:t&mynews=0&start="
#str1 = "https://search.naver.com/search.naver?&where=news&query=%EB%B3%B5%EB%A9%B4%EA%B0%80%EC%99%95&sm=tab_pge&sort=2&photo=0&field=1&reporter_article=&pd=3&ds=2017.10.01&de=2017.12.28&docid=&nso=so:da,p:from20171001to20171228,a:t&mynews=0&start="

str2 = "&refresh_start=0"

for i in range(1, 3342, 10):  #this can be changed (0 - 3341,3122,2428,1453)
    strurl = str1 + str(i) + str2
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
f = open('bokmyengawang_url1.txt', 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()



#2
url_list = []

#str1 = "https://search.naver.com/search.naver?&where=news&query=%EB%B3%B5%EB%A9%B4%EA%B0%80%EC%99%95&sm=tab_pge&sort=2&photo=0&field=1&reporter_article=&pd=3&ds=2017.01.01&de=2017.03.31&docid=&nso=so:da,p:from20170101to20170331,a:t&mynews=0&start="
str1 = "https://search.naver.com/search.naver?&where=news&query=%EB%B3%B5%EB%A9%B4%EA%B0%80%EC%99%95&sm=tab_pge&sort=2&photo=0&field=1&reporter_article=&pd=3&ds=2017.04.01&de=2017.06.30&docid=&nso=so:da,p:from20170401to20170630,a:t&mynews=0&start="
#str1 = "https://search.naver.com/search.naver?&where=news&query=%EB%B3%B5%EB%A9%B4%EA%B0%80%EC%99%95&sm=tab_pge&sort=2&photo=0&field=1&reporter_article=&pd=3&ds=2017.07.01&de=2017.09.30&docid=&nso=so:da,p:from20170701to20170930,a:t&mynews=0&start="
#str1 = "https://search.naver.com/search.naver?&where=news&query=%EB%B3%B5%EB%A9%B4%EA%B0%80%EC%99%95&sm=tab_pge&sort=2&photo=0&field=1&reporter_article=&pd=3&ds=2017.10.01&de=2017.12.28&docid=&nso=so:da,p:from20171001to20171228,a:t&mynews=0&start="

str2 = "&refresh_start=0"

for i in range(1, 3123, 10):  #this can be changed (0 - 3341,3122,2428,1453)
    strurl = str1 + str(i) + str2
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
f = open('bokmyengawang_url2.txt', 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()






#3
url_list = []

#str1 = "https://search.naver.com/search.naver?&where=news&query=%EB%B3%B5%EB%A9%B4%EA%B0%80%EC%99%95&sm=tab_pge&sort=2&photo=0&field=1&reporter_article=&pd=3&ds=2017.01.01&de=2017.03.31&docid=&nso=so:da,p:from20170101to20170331,a:t&mynews=0&start="
#str1 = "https://search.naver.com/search.naver?&where=news&query=%EB%B3%B5%EB%A9%B4%EA%B0%80%EC%99%95&sm=tab_pge&sort=2&photo=0&field=1&reporter_article=&pd=3&ds=2017.04.01&de=2017.06.30&docid=&nso=so:da,p:from20170401to20170630,a:t&mynews=0&start="
str1 = "https://search.naver.com/search.naver?&where=news&query=%EB%B3%B5%EB%A9%B4%EA%B0%80%EC%99%95&sm=tab_pge&sort=2&photo=0&field=1&reporter_article=&pd=3&ds=2017.07.01&de=2017.09.30&docid=&nso=so:da,p:from20170701to20170930,a:t&mynews=0&start="
#str1 = "https://search.naver.com/search.naver?&where=news&query=%EB%B3%B5%EB%A9%B4%EA%B0%80%EC%99%95&sm=tab_pge&sort=2&photo=0&field=1&reporter_article=&pd=3&ds=2017.10.01&de=2017.12.28&docid=&nso=so:da,p:from20171001to20171228,a:t&mynews=0&start="

str2 = "&refresh_start=0"

for i in range(1, 2429, 10):  #this can be changed (0 - 3341,3122,2428,1453)
    strurl = str1 + str(i) + str2
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
f = open('bokmyengawang_url3.txt', 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()



#4
url_list = []

#str1 = "https://search.naver.com/search.naver?&where=news&query=%EB%B3%B5%EB%A9%B4%EA%B0%80%EC%99%95&sm=tab_pge&sort=2&photo=0&field=1&reporter_article=&pd=3&ds=2017.01.01&de=2017.03.31&docid=&nso=so:da,p:from20170101to20170331,a:t&mynews=0&start="
#str1 = "https://search.naver.com/search.naver?&where=news&query=%EB%B3%B5%EB%A9%B4%EA%B0%80%EC%99%95&sm=tab_pge&sort=2&photo=0&field=1&reporter_article=&pd=3&ds=2017.04.01&de=2017.06.30&docid=&nso=so:da,p:from20170401to20170630,a:t&mynews=0&start="
#str1 = "https://search.naver.com/search.naver?&where=news&query=%EB%B3%B5%EB%A9%B4%EA%B0%80%EC%99%95&sm=tab_pge&sort=2&photo=0&field=1&reporter_article=&pd=3&ds=2017.07.01&de=2017.09.30&docid=&nso=so:da,p:from20170701to20170930,a:t&mynews=0&start="
str1 = "https://search.naver.com/search.naver?&where=news&query=%EB%B3%B5%EB%A9%B4%EA%B0%80%EC%99%95&sm=tab_pge&sort=2&photo=0&field=1&reporter_article=&pd=3&ds=2017.10.01&de=2017.12.28&docid=&nso=so:da,p:from20171001to20171228,a:t&mynews=0&start="

str2 = "&refresh_start=0"

for i in range(1, 1454, 10):  #this can be changed (0 - 3341,3122,2428,1453)
    strurl = str1 + str(i) + str2
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
f = open('bokmyengawang_url4.txt', 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
