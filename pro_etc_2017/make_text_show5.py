from bs4 import BeautifulSoup
import urllib.request

#1quarter

pro1 = 'balchick'
pro2 = 'voguemom'
pro3 = 'semobang'
pro4 = 'sectiontv'
pro5 = 'showmusic'
pro6 = 'ojimagic'

urlfile = '{}2017_url{}.txt'
textfile = '{}2017_text{}qt.txt'





with open(urlfile.format(pro5, '4'), 'r') as f:
    naver_url_show4 = f.readlines()
   

#4qt    
naver_url_list = []
for i in naver_url_show4:
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
        
with open(textfile.format(pro5, '4'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)

