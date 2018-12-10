from bs4 import BeautifulSoup
import urllib.request

#1quarter

pro = 'muhan' #이 부분을 바꾸세요.
urlfile = '{}2016_url{}.txt'
textfile = '{}2016_text{}qt.txt'


#2016년은 월별로 되어 있어서 이렇게 많지만, 2017년은 분기별로 뽑아도 될 것 같습니다. 

with open(urlfile.format(pro, '1'), 'r') as f:
    naver_url1 = f.readlines()
with open(urlfile.format(pro, '2'), 'r') as f:
    naver_url2 = f.readlines()
with open(urlfile.format(pro, '3'), 'r') as f:
    naver_url3 = f.readlines()
naver_url1qt = naver_url1 + naver_url2 + naver_url3

with open(urlfile.format(pro, '4'), 'r') as f:
    naver_url4 = f.readlines()
with open(urlfile.format(pro, '5'), 'r') as f:
    naver_url5 = f.readlines()
with open(urlfile.format(pro, '6'), 'r') as f:
    naver_url6 = f.readlines()
naver_url2qt = naver_url4 + naver_url5 + naver_url6

with open(urlfile.format(pro, '7'), 'r') as f:
    naver_url1 = f.readlines()
with open(urlfile.format(pro, '8'), 'r') as f:
    naver_url2 = f.readlines()
with open(urlfile.format(pro, '9'), 'r') as f:
    naver_url3 = f.readlines()
naver_url3qt = naver_url7 + naver_url8 + naver_url9

with open(urlfile.format(pro, '10'), 'r') as f:
    naver_url10 = f.readlines()
with open(urlfile.format(pro, '11'), 'r') as f:
    naver_url11 = f.readlines()
with open(urlfile.format(pro, '12'), 'r') as f:
    naver_url12 = f.readlines()
naver_url4qt = naver_url10 + naver_url11 + naver_url12

#1qt    
naver_url_list = []
for i in naver_url1qt:
    naver_url_list.append(i[0:len(i)-1])

print(len(naver_url_list))
    
text_list = []         
for i in range(len(naver_url_list)):
    print(i)
    try:
        with urllib.request.urlopen(naver_url_list[i]) as url:
            doc = url.read()
            soup = BeautifulSoup(doc, "html.parser")
            try:
                divs = soup.find_all("div", class_="article_body font1 size3")
                for div in divs:
                    body = div.text.strip()
                    text_list.append(body)
            except:
                pass
    except:
        pass
        
with open(textfile.format(pro, '1'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)

#2qt    
naver_url_list = []
for i in naver_url2qt:
    naver_url_list.append(i[0:len(i)-1])

print(len(naver_url_list))
    
text_list = []         
for i in range(len(naver_url_list)):
    print(i)
    try:
        with urllib.request.urlopen(naver_url_list[i]) as url:
            doc = url.read()
            soup = BeautifulSoup(doc, "html.parser")
            try:
                divs = soup.find_all("div", class_="article_body font1 size3")
                for div in divs:
                    body = div.text.strip()
                    text_list.append(body)
            except:
                pass
    except:
        pass
        
with open(textfile.format(pro, '2'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)

#3qt    
naver_url_list = []
for i in naver_url3qt:
    naver_url_list.append(i[0:len(i)-1])

print(len(naver_url_list))
    
text_list = []         
for i in range(len(naver_url_list)):
    print(i)
    try:
        with urllib.request.urlopen(naver_url_list[i]) as url:
            doc = url.read()
            soup = BeautifulSoup(doc, "html.parser")
            try:
                divs = soup.find_all("div", class_="article_body font1 size3")
                for div in divs:
                    body = div.text.strip()
                    text_list.append(body)
            except:
                pass
    except:
        pass
        
with open(textfile.format(pro, '3'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)    

#4qt    
naver_url_list = []
for i in naver_url4qt:
    naver_url_list.append(i[0:len(i)-1])

print(len(naver_url_list))
    
text_list = []         
for i in range(len(naver_url_list)):
    print(i)
    try:
        with urllib.request.urlopen(naver_url_list[i]) as url:
            doc = url.read()
            soup = BeautifulSoup(doc, "html.parser")
            try:
                divs = soup.find_all("div", class_="article_body font1 size3")
                for div in divs:
                    body = div.text.strip()
                    text_list.append(body)
            except:
                pass
    except:
        pass
        
with open(textfile.format(pro, '4'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)