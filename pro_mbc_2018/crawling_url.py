from bs4 import BeautifulSoup
import urllib.request
from urllib import parse

pro1 = 'nahonja'
pro2 = 'radiostar'
pro3 = 'bokmyen'
pro4 = 'sectiontv'
pro5 = 'showmusic'
pro61 = 'jeoncham1'
pro62 = 'jeoncham2'
pro7 = 'unexpectq'
pro8 = 'dunia'
pro9 = 'realman'
pro10 = 'nomad'
pro11 = 'hungers'
pro12 = 'daejang'
pro13 = 'gungmin'
pro14 = 'undernine'

count = {'pro11': 4001, 'pro12': 4001, 'pro13': 4001, 'pro14': 3737,
        'pro21': 2973, 'pro22': 3052, 'pro23': 3968, 'pro24': 2259,
        'pro31': 2759, 'pro32': 3204, 'pro33': 2779, 'pro34': 2569,
        'pro41': 392, 'pro42': 630, 'pro43': 601, 'pro44': 698,
        'pro51': 127, 'pro52': 110, 'pro53': 132, 'pro54': 148,
        'pro611': 965, 'pro612': 1585, 'pro613': 1479, 'pro614': 1005,
        'pro621': 120, 'pro622': 1971, 'pro623': 1704, 'pro624': 1394,
        'pro71': 0, 'pro72': 1997, 'pro73': 1275, 'pro74': 345,
        'pro81': 0, 'pro82': 1484, 'pro83': 1134, 'pro84': 18,
        'pro91': 0, 'pro92': 0, 'pro93': 1294, 'pro94': 1634,
        'pro101': 0, 'pro102': 0, 'pro103': 266, 'pro104': 505,
        'pro111': 0, 'pro112': 0, 'pro113': 210, 'pro114': 881,
        'pro121': 0, 'pro122': 0, 'pro123': 134, 'pro124': 1131,
        'pro131': 0, 'pro132': 0, 'pro133': 0, 'pro134': 1451,
        'pro141': 0, 'pro142': 3, 'pro143': 185, 'pro144': 2205}



str1 = 'https://search.naver.com/search.naver?&where=news&query={}'
#program name

pro1_parse = parse.quote("나혼자산다")
pro2_parse = parse.quote("라디오스타")
pro3_parse = parse.quote("복면가왕")
pro4_parse = '%EC%84%B9%EC%85%98tv'
pro5_parse = parse.quote("쇼음악중심")
pro6_parse = parse.quote("전지적참견시점")
pro6_parse2 = parse.quote("전참시")
pro7_parse = parse.quote("뜻밖의") + 'Q'
pro8_parse = parse.quote("두니아")
pro9_parse = parse.quote("진짜사나이") + '300'
pro10_parse = parse.quote("토크노마드")
pro11_parse = parse.quote("공복자들")
pro12_parse = parse.quote("대장금이보고있다")
pro13_parse = parse.quote("궁민남편")
pro14_parse = parse.quote("언더나인틴")


str2 = '&sm=tab_pge&sort=2&photo=0&field=1&reporter_article=&pd=3&ds={}'

#quarter
quarter1 = ['2018.01.01&de=2018.03.31', '20180101to20180331']
quarter2 = ['2018.04.01&de=2018.06.30', '20180301to20180630']
quarter3 = ['2018.07.01&de=2018.09.30', '20180601to20180930']
quarter4 = ['2018.10.01&de=2018.12.28', '20181001to20181228']

str3 = '&docid=&nso=so:da,p:from{}'

str4 = ',a:t&mynews=0&start={}'

str5 = '&refresh_start=0'

urlfile = '{}2018_url{}.txt'

#'https://search.naver.com/search.naver?&where=news&query={}&sm=tab_pge&sort=2&photo=0&field=1&reporter_article=&pd=3&ds={}&docid=&nso=so:da,p:from{},a:t&mynews=0&start={}&refresh_start=0'


#1qt_nahon

url_list = []
for i in range(1, count['pro11'], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(pro1_parse, quarter1[0], quarter1[1], str(i))
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
f = open(urlfile.format(pro1, '1'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('1')


#2qt

url_list = []
for i in range(1, count['pro12'], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(pro1_parse, quarter2[0], quarter2[1], str(i))
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
f = open(urlfile.format(pro1, '2'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('2')


#3qt

url_list = []
for i in range(1, count['pro13'], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(pro1_parse, quarter3[0], quarter3[1], str(i))
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
f = open(urlfile.format(pro1, '3'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('3')

#1qt

url_list = []
for i in range(1, count['pro14'], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(pro1_parse, quarter4[0], quarter4[1], str(i))
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
f = open(urlfile.format(pro1, '4'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('4')

#1qt_duet

url_list = []
for i in range(1, count['pro21'], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(pro2_parse, quarter1[0], quarter1[1], str(i))
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
f = open(urlfile.format(pro2, '1'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('1')


#2qt

url_list = []
for i in range(1, count['pro22'], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(pro2_parse, quarter2[0], quarter2[1], str(i))
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
f = open(urlfile.format(pro2, '2'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('2')


#3qt

url_list = []
for i in range(1, count['pro23'], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(pro2_parse, quarter3[0], quarter3[1], str(i))
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
f = open(urlfile.format(pro2, '3'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('3')

#4qt

url_list = []
for i in range(1, count['pro24'], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(pro2_parse, quarter4[0], quarter4[1], str(i))
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
f = open(urlfile.format(pro2, '4'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('4')

#1qt_sectiontv

url_list = []
for i in range(1, count['pro31'], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(pro3_parse, quarter1[0], quarter1[1], str(i))
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
f = open(urlfile.format(pro3, '1'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('1')


#2qt

url_list = []
for i in range(1, count['pro32'], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(pro3_parse, quarter2[0], quarter2[1], str(i))
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
f = open(urlfile.format(pro3, '2'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('2')


#3qt

url_list = []
for i in range(1, count['pro33'], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(pro3_parse, quarter3[0], quarter3[1], str(i))
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
f = open(urlfile.format(pro3, '3'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('3')

#4qt

url_list = []
for i in range(1, count['pro34'], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(pro3_parse, quarter4[0], quarter4[1], str(i))
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
f = open(urlfile.format(pro3, '4'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('4')

#1qt_show

url_list = []
for i in range(1, count['pro41'], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(pro4_parse, quarter1[0], quarter1[1], str(i))
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
f = open(urlfile.format(pro4, '1'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('1')


#2qt_section

url_list = []
for i in range(1, count['pro42'], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(pro4_parse, quarter2[0], quarter2[1], str(i))
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
f = open(urlfile.format(pro4, '2'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('2')


#3qt_section

url_list = []
for i in range(1, count['pro43'], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(pro4_parse, quarter3[0], quarter3[1], str(i))
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
f = open(urlfile.format(pro4, '3'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('3')

#4qt_section

url_list = []
for i in range(1, count['pro44'], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(pro4_parse, quarter4[0], quarter4[1], str(i))
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
f = open(urlfile.format(pro4, '4'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('4')

#1qt
url_list = []
for i in range(1, count['pro51'], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(pro5_parse, quarter1[0], quarter1[1], str(i))
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
f = open(urlfile.format(pro5, '1'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('1')

#2qt_show
url_list = []
for i in range(1, count['pro52'], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(pro5_parse, quarter2[0], quarter2[1], str(i))
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
f = open(urlfile.format(pro5, '2'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('2')

#3qt
url_list = []
for i in range(1, count['pro53'], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(pro5_parse, quarter3[0], quarter3[1], str(i))
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
f = open(urlfile.format(pro5, '3'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('3')

#4qt
url_list = []
for i in range(1, count['pro54'], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(pro5_parse, quarter4[0], quarter4[1], str(i))
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


#1qt
url_list = []
for i in range(1, count['pro611'], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(pro6_parse, quarter1[0], quarter1[1], str(i))
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
f = open(urlfile.format(pro61, '1'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('1')


#2qt

url_list = []
for i in range(1, count['pro612'], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(pro6_parse, quarter2[0], quarter2[1], str(i))
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
f = open(urlfile.format(pro61, '2'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('2')


#3qt

url_list = []
for i in range(1, count['pro613'], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(pro6_parse, quarter3[0], quarter3[1], str(i))
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
f = open(urlfile.format(pro61, '3'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('3')

#4qt

url_list = []
for i in range(1, count['pro614'], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(pro6_parse, quarter4[0], quarter4[1], str(i))
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
f = open(urlfile.format(pro61, '4'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('4')

#1
url_list = []
for i in range(1, count['pro621'], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(pro6_parse2, quarter4[0], quarter4[1], str(i))
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
f = open(urlfile.format(pro62, '1'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('1')

url_list = []
for i in range(1, count['pro622'], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(pro6_parse2, quarter4[0], quarter4[1], str(i))
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
f = open(urlfile.format(pro62, '2'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('2')

url_list = []
for i in range(1, count['pro623'], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(pro6_parse2, quarter4[0], quarter4[1], str(i))
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
f = open(urlfile.format(pro62, '3'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('3')

url_list = []
for i in range(1, count['pro624'], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(pro6_parse2, quarter4[0], quarter4[1], str(i))
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
f = open(urlfile.format(pro62, '4'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('4')


#1qt
url_list = []
for i in range(1, count['pro71'], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(pro7_parse, quarter1[0], quarter1[1], str(i))
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
f = open(urlfile.format(pro7, '1'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('1')

#2qt_show
url_list = []
for i in range(1, count['pro72'], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(pro7_parse, quarter2[0], quarter2[1], str(i))
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
f = open(urlfile.format(pro7, '2'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('2')

#3qt
url_list = []
for i in range(1, count['pro73'], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(pro7_parse, quarter3[0], quarter3[1], str(i))
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
f = open(urlfile.format(pro7, '3'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('3')

#4qt
url_list = []
for i in range(1, count['pro74'], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(pro7_parse, quarter4[0], quarter4[1], str(i))
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
f = open(urlfile.format(pro7, '4'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('4')


#1qt
url_list = []
for i in range(1, count['pro81'], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(pro8_parse, quarter1[0], quarter1[1], str(i))
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
f = open(urlfile.format(pro8, '1'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('1')

#2qt_show
url_list = []
for i in range(1, count['pro82'], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(pro8_parse, quarter2[0], quarter2[1], str(i))
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
f = open(urlfile.format(pro8, '2'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('2')

#3qt
url_list = []
for i in range(1, count['pro83'], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(pro8_parse, quarter3[0], quarter3[1], str(i))
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
f = open(urlfile.format(pro8, '3'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('3')

#4qt
url_list = []
for i in range(1, count['pro84'], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(pro8_parse, quarter4[0], quarter4[1], str(i))
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
f = open(urlfile.format(pro8, '4'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('4')


#1qt
url_list = []
for i in range(1, count['pro91'], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(pro9_parse, quarter1[0], quarter1[1], str(i))
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
f = open(urlfile.format(pro9, '1'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('1')

#2qt_show
url_list = []
for i in range(1, count['pro92'], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(pro9_parse, quarter2[0], quarter2[1], str(i))
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
f = open(urlfile.format(pro9, '2'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('2')

#3qt
url_list = []
for i in range(1, count['pro93'], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(pro9_parse, quarter3[0], quarter3[1], str(i))
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
f = open(urlfile.format(pro9, '3'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('3')

#4qt
url_list = []
for i in range(1, count['pro94'], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(pro9_parse, quarter4[0], quarter4[1], str(i))
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
f = open(urlfile.format(pro9, '4'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('4')


#1qt
url_list = []
for i in range(1, count['pro101'], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(pro10_parse, quarter1[0], quarter1[1], str(i))
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
f = open(urlfile.format(pro10, '1'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('1')

#2qt_show
url_list = []
for i in range(1, count['pro102'], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(pro10_parse, quarter2[0], quarter2[1], str(i))
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
f = open(urlfile.format(pro10, '2'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('2')

#3qt
url_list = []
for i in range(1, count['pro103'], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(pro10_parse, quarter3[0], quarter3[1], str(i))
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
f = open(urlfile.format(pro10, '3'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('3')

#4qt
url_list = []
for i in range(1, count['pro104'], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(pro10_parse, quarter4[0], quarter4[1], str(i))
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
f = open(urlfile.format(pro10, '4'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('4')


#1qt
url_list = []
for i in range(1, count['pro111'], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(pro11_parse, quarter1[0], quarter1[1], str(i))
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
f = open(urlfile.format(pro11, '1'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('1')

#2qt_show
url_list = []
for i in range(1, count['pro112'], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(pro11_parse, quarter2[0], quarter2[1], str(i))
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
f = open(urlfile.format(pro11, '2'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('2')

#3qt
url_list = []
for i in range(1, count['pro113'], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(pro11_parse, quarter3[0], quarter3[1], str(i))
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
f = open(urlfile.format(pro11, '3'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('3')

#4qt
url_list = []
for i in range(1, count['pro114'], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(pro11_parse, quarter4[0], quarter4[1], str(i))
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
f = open(urlfile.format(pro11, '4'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('4')


#1qt
url_list = []
for i in range(1, count['pro121'], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(pro12_parse, quarter1[0], quarter1[1], str(i))
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
f = open(urlfile.format(pro12, '1'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('1')

#2qt_show
url_list = []
for i in range(1, count['pro122'], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(pro12_parse, quarter2[0], quarter2[1], str(i))
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
f = open(urlfile.format(pro12, '2'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('2')

#3qt
url_list = []
for i in range(1, count['pro123'], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(pro12_parse, quarter3[0], quarter3[1], str(i))
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
f = open(urlfile.format(pro12, '3'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('3')

#4qt
url_list = []
for i in range(1, count['pro124'], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(pro12_parse, quarter4[0], quarter4[1], str(i))
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
f = open(urlfile.format(pro12, '4'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('4')


#1qt
url_list = []
for i in range(1, count['pro131'], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(pro13_parse, quarter1[0], quarter1[1], str(i))
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
f = open(urlfile.format(pro13, '1'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('1')

#2qt_show
url_list = []
for i in range(1, count['pro132'], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(pro13_parse, quarter2[0], quarter2[1], str(i))
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
f = open(urlfile.format(pro13, '2'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('2')

#3qt
url_list = []
for i in range(1, count['pro133'], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(pro13_parse, quarter3[0], quarter3[1], str(i))
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
f = open(urlfile.format(pro13, '3'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('3')

#4qt
url_list = []
for i in range(1, count['pro134'], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(pro13_parse, quarter4[0], quarter4[1], str(i))
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
f = open(urlfile.format(pro13, '4'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('4')


#1qt
url_list = []
for i in range(1, count['pro141'], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(pro14_parse, quarter1[0], quarter1[1], str(i))
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
f = open(urlfile.format(pro14, '1'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('1')

#2qt_show
url_list = []
for i in range(1, count['pro142'], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(pro14_parse, quarter2[0], quarter2[1], str(i))
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
f = open(urlfile.format(pro14, '2'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('2')

#3qt
url_list = []
for i in range(1, count['pro143'], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(pro14_parse, quarter3[0], quarter3[1], str(i))
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
f = open(urlfile.format(pro14, '3'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('3')

#4qt
url_list = []
for i in range(1, count['pro144'], 10):  
    strall = str1 + str2 + str3 + str4 + str5
    strurl = strall.format(pro14_parse, quarter4[0], quarter4[1], str(i))
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
f = open(urlfile.format(pro14, '4'), 'w', encoding='utf-8')
for i in news_url:
    data = i + '\n'
    f.write(data)
f.close()
print('4')
