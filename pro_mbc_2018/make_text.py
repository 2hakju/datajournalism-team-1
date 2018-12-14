from bs4 import BeautifulSoup
import urllib.request

#1quarter

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


urlfile = '{}2018_url{}.txt'
textfile = '{}2018_text{}qt.txt'



with open(urlfile.format(pro1, '1'), 'r') as f:
    naver_url_pro11 = f.readlines()
with open(urlfile.format(pro1, '2'), 'r') as f:
    naver_url_pro12 = f.readlines()
with open(urlfile.format(pro1, '3'), 'r') as f:
    naver_url_pro13 = f.readlines()
with open(urlfile.format(pro1, '4'), 'r') as f:
    naver_url_pro14 = f.readlines()


with open(urlfile.format(pro2, '1'), 'r') as f:
    naver_url_pro21 = f.readlines()
with open(urlfile.format(pro2, '2'), 'r') as f:
    naver_url_pro22 = f.readlines()
with open(urlfile.format(pro2, '3'), 'r') as f:
    naver_url_pro23 = f.readlines()
with open(urlfile.format(pro2, '4'), 'r') as f:
    naver_url_pro24 = f.readlines()


with open(urlfile.format(pro3, '1'), 'r') as f:
    naver_url_pro31 = f.readlines()
with open(urlfile.format(pro3, '2'), 'r') as f:
    naver_url_pro32 = f.readlines()
with open(urlfile.format(pro3, '3'), 'r') as f:
    naver_url_pro33 = f.readlines()
with open(urlfile.format(pro3, '4'), 'r') as f:
    naver_url_pro34 = f.readlines()


with open(urlfile.format(pro4, '1'), 'r') as f:
    naver_url_pro41 = f.readlines()
with open(urlfile.format(pro4, '2'), 'r') as f:
    naver_url_pro42 = f.readlines()
with open(urlfile.format(pro4, '3'), 'r') as f:
    naver_url_pro43 = f.readlines()
with open(urlfile.format(pro4, '4'), 'r') as f:
    naver_url_pro44 = f.readlines()


with open(urlfile.format(pro5, '1'), 'r') as f:
    naver_url_pro51 = f.readlines()
with open(urlfile.format(pro5, '2'), 'r') as f:
    naver_url_pro52 = f.readlines()
with open(urlfile.format(pro5, '3'), 'r') as f:
    naver_url_pro53 = f.readlines()
with open(urlfile.format(pro5, '4'), 'r') as f:
    naver_url_pro54 = f.readlines()


with open(urlfile.format(pro61, '1'), 'r') as f:
    naver_url_pro611 = f.readlines()
with open(urlfile.format(pro61, '2'), 'r') as f:
    naver_url_pro612 = f.readlines()
with open(urlfile.format(pro61, '3'), 'r') as f:
    naver_url_pro613 = f.readlines()
with open(urlfile.format(pro61, '4'), 'r') as f:
    naver_url_pro614 = f.readlines()

with open(urlfile.format(pro62, '1'), 'r') as f:
    naver_url_pro621 = f.readlines()
with open(urlfile.format(pro62, '2'), 'r') as f:
    naver_url_pro622 = f.readlines()
with open(urlfile.format(pro62, '3'), 'r') as f:
    naver_url_pro623 = f.readlines()
with open(urlfile.format(pro62, '4'), 'r') as f:
    naver_url_pro624 = f.readlines()

with open(urlfile.format(pro7, '1'), 'r') as f:
    naver_url_pro71 = f.readlines()
with open(urlfile.format(pro7, '2'), 'r') as f:
    naver_url_pro72 = f.readlines()
with open(urlfile.format(pro7, '3'), 'r') as f:
    naver_url_pro73 = f.readlines()
with open(urlfile.format(pro7, '4'), 'r') as f:
    naver_url_pro74 = f.readlines()


with open(urlfile.format(pro8, '1'), 'r') as f:
    naver_url_pro81 = f.readlines()
with open(urlfile.format(pro8, '2'), 'r') as f:
    naver_url_pro82 = f.readlines()
with open(urlfile.format(pro8, '3'), 'r') as f:
    naver_url_pro83 = f.readlines()
with open(urlfile.format(pro8, '4'), 'r') as f:
    naver_url_pro84 = f.readlines()


with open(urlfile.format(pro9, '1'), 'r') as f:
    naver_url_pro91 = f.readlines()
with open(urlfile.format(pro9, '2'), 'r') as f:
    naver_url_pro92 = f.readlines()
with open(urlfile.format(pro9, '3'), 'r') as f:
    naver_url_pro93 = f.readlines()
with open(urlfile.format(pro9, '4'), 'r') as f:
    naver_url_pro94 = f.readlines()


with open(urlfile.format(pro10, '1'), 'r') as f:
    naver_url_pro101 = f.readlines()
with open(urlfile.format(pro10, '2'), 'r') as f:
    naver_url_pro102 = f.readlines()
with open(urlfile.format(pro10, '3'), 'r') as f:
    naver_url_pro103 = f.readlines()
with open(urlfile.format(pro10, '4'), 'r') as f:
    naver_url_pro104 = f.readlines()


with open(urlfile.format(pro11, '1'), 'r') as f:
    naver_url_pro111 = f.readlines()
with open(urlfile.format(pro11, '2'), 'r') as f:
    naver_url_pro112 = f.readlines()
with open(urlfile.format(pro11, '3'), 'r') as f:
    naver_url_pro113 = f.readlines()
with open(urlfile.format(pro11, '4'), 'r') as f:
    naver_url_pro114 = f.readlines()


with open(urlfile.format(pro12, '1'), 'r') as f:
    naver_url_pro121 = f.readlines()
with open(urlfile.format(pro12, '2'), 'r') as f:
    naver_url_pro122 = f.readlines()
with open(urlfile.format(pro12, '3'), 'r') as f:
    naver_url_pro123 = f.readlines()
with open(urlfile.format(pro12, '4'), 'r') as f:
    naver_url_pro124 = f.readlines()


with open(urlfile.format(pro13, '1'), 'r') as f:
    naver_url_pro131 = f.readlines()
with open(urlfile.format(pro13, '2'), 'r') as f:
    naver_url_pro132 = f.readlines()
with open(urlfile.format(pro13, '3'), 'r') as f:
    naver_url_pro133 = f.readlines()
with open(urlfile.format(pro13, '4'), 'r') as f:
    naver_url_pro134 = f.readlines()


with open(urlfile.format(pro14, '1'), 'r') as f:
    naver_url_pro141 = f.readlines()
with open(urlfile.format(pro14, '2'), 'r') as f:
    naver_url_pro142 = f.readlines()
with open(urlfile.format(pro14, '3'), 'r') as f:
    naver_url_pro143 = f.readlines()
with open(urlfile.format(pro14, '4'), 'r') as f:
    naver_url_pro144 = f.readlines()




#1qt_balch    
naver_url_list = []
for i in naver_url_pro11:
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
        
with open(textfile.format(pro1, '1'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)

#2qt    
naver_url_list = []
for i in naver_url_pro12:
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
        
with open(textfile.format(pro1, '2'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)

#3qt    
naver_url_list = []
for i in naver_url_pro13:
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
        
with open(textfile.format(pro1, '3'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)    

#4qt    
naver_url_list = []
for i in naver_url_pro14:
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
        
with open(textfile.format(pro1, '4'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)


#1qt    
naver_url_list = []
for i in naver_url_pro21:
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
        
with open(textfile.format(pro2, '1'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)

#2qt    
naver_url_list = []
for i in naver_url_pro22:
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
        
with open(textfile.format(pro2, '2'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)

#3qt    
naver_url_list = []
for i in naver_url_pro23:
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
        
with open(textfile.format(pro2, '3'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)    

#4qt    
naver_url_list = []
for i in naver_url_pro24:
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
        
with open(textfile.format(pro2, '4'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)

#1qt
naver_url_list = []
for i in naver_url_pro31:
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
        
with open(textfile.format(pro3, '1'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)

#2qt    
naver_url_list = []
for i in naver_url_pro32:
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
        
with open(textfile.format(pro3, '2'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)

#3qt    
naver_url_list = []
for i in naver_url_pro33:
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
        
with open(textfile.format(pro3, '3'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)    

#4qt    
naver_url_list = []
for i in naver_url_pro34:
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
        
with open(textfile.format(pro3, '4'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)

#1qt_section    
naver_url_list = []
for i in naver_url_pro41:
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
        
with open(textfile.format(pro4, '1'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)

#2qt    
naver_url_list = []
for i in naver_url_pro42:
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
        
with open(textfile.format(pro4, '2'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)

#3qt    
naver_url_list = []
for i in naver_url_pro43:
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
        
with open(textfile.format(pro4, '3'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)    

#4qt    
naver_url_list = []
for i in naver_url_pro44:
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
        
with open(textfile.format(pro4, '4'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)

#1qt_show    
naver_url_list = []
for i in naver_url_pro51:
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
        
with open(textfile.format(pro5, '1'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)

#2qt    
naver_url_list = []
for i in naver_url_pro52:
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
        
with open(textfile.format(pro5, '2'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)

#3qt    
naver_url_list = []
for i in naver_url_pro53:
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
        
with open(textfile.format(pro5, '3'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)    

#4qt    
naver_url_list = []
for i in naver_url_pro54:
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

#1qt
naver_url_list = []
for i in naver_url_pro611:
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
        
with open(textfile.format(pro61, '1'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)

#2qt    
naver_url_list = []
for i in naver_url_pro612:
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
        
with open(textfile.format(pro61, '2'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)


#3qt    
naver_url_list = []
for i in naver_url_pro613:
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
        
with open(textfile.format(pro61, '3'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)    

#4qt    
naver_url_list = []
for i in naver_url_pro614:
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
        
with open(textfile.format(pro61, '4'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)

#1qt
naver_url_list = []
for i in naver_url_pro621:
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
        
with open(textfile.format(pro62, '1'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)

#2qt    
naver_url_list = []
for i in naver_url_pro622:
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
        
with open(textfile.format(pro62, '2'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)


#3qt    
naver_url_list = []
for i in naver_url_pro623:
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
        
with open(textfile.format(pro62, '3'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)    

#4qt    
naver_url_list = []
for i in naver_url_pro624:
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
        
with open(textfile.format(pro62, '4'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)

#1qt_balch    
naver_url_list = []
for i in naver_url_pro71:
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
        
with open(textfile.format(pro7, '1'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)

#2qt    
naver_url_list = []
for i in naver_url_pro72:
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
        
with open(textfile.format(pro7, '2'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)

#3qt    
naver_url_list = []
for i in naver_url_pro73:
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
        
with open(textfile.format(pro7, '3'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)    

#4qt    
naver_url_list = []
for i in naver_url_pro74:
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
        
with open(textfile.format(pro7, '4'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)


#1qt    
naver_url_list = []
for i in naver_url_pro81:
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
        
with open(textfile.format(pro8, '1'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)

#2qt    
naver_url_list = []
for i in naver_url_pro82:
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
        
with open(textfile.format(pro8, '2'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)

#3qt    
naver_url_list = []
for i in naver_url_pro83:
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
        
with open(textfile.format(pro8, '3'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)    

#4qt    
naver_url_list = []
for i in naver_url_pro84:
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
        
with open(textfile.format(pro8, '4'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)

#1qt
naver_url_list = []
for i in naver_url_pro91:
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
        
with open(textfile.format(pro9, '1'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)

#2qt    
naver_url_list = []
for i in naver_url_pro92:
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
        
with open(textfile.format(pro9, '2'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)

#3qt    
naver_url_list = []
for i in naver_url_pro93:
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
        
with open(textfile.format(pro9, '3'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)    

#4qt    
naver_url_list = []
for i in naver_url_pro94:
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
        
with open(textfile.format(pro9, '4'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)

#1qt_section    
naver_url_list = []
for i in naver_url_pro101:
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
        
with open(textfile.format(pro10, '1'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)

#2qt    
naver_url_list = []
for i in naver_url_pro102:
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
        
with open(textfile.format(pro10, '2'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)

#3qt    
naver_url_list = []
for i in naver_url_pro103:
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
        
with open(textfile.format(pro10, '3'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)    

#4qt    
naver_url_list = []
for i in naver_url_pro104:
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
        
with open(textfile.format(pro10, '4'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)

#1qt_show    
naver_url_list = []
for i in naver_url_pro111:
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
        
with open(textfile.format(pro11, '1'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)

#2qt    
naver_url_list = []
for i in naver_url_pro112:
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
        
with open(textfile.format(pro11, '2'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)

#3qt    
naver_url_list = []
for i in naver_url_pro113:
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
        
with open(textfile.format(pro11, '3'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)    

#4qt    
naver_url_list = []
for i in naver_url_pro114:
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
        
with open(textfile.format(pro11, '4'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)

#1qt
naver_url_list = []
for i in naver_url_pro121:
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
        
with open(textfile.format(pro12, '1'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)

#2qt    
naver_url_list = []
for i in naver_url_pro122:
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
        
with open(textfile.format(pro12, '2'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)


#3qt    
naver_url_list = []
for i in naver_url_pro123:
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
        
with open(textfile.format(pro12, '3'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)    

#4qt    
naver_url_list = []
for i in naver_url_pro124:
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
        
with open(textfile.format(pro12, '4'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)

#1qt
naver_url_list = []
for i in naver_url_pro131:
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
        
with open(textfile.format(pro13, '1'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)

#2qt    
naver_url_list = []
for i in naver_url_pro132:
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
        
with open(textfile.format(pro13, '2'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)


#3qt    
naver_url_list = []
for i in naver_url_pro133:
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
        
with open(textfile.format(pro13, '3'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)    

#4qt    
naver_url_list = []
for i in naver_url_pro134:
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
        
with open(textfile.format(pro13, '4'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)

#14
naver_url_list = []
for i in naver_url_pro141:
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
        
with open(textfile.format(pro14, '1'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)

#2qt    
naver_url_list = []
for i in naver_url_pro142:
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
        
with open(textfile.format(pro14, '2'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)


#3qt    
naver_url_list = []
for i in naver_url_pro143:
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
        
with open(textfile.format(pro14, '3'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)    

#4qt    
naver_url_list = []
for i in naver_url_pro144:
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
        
with open(textfile.format(pro14, '4'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)