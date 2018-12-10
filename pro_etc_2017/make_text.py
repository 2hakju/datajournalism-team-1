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


'''
with open(urlfile.format(pro1, '1'), 'r') as f:
    naver_url_balch1 = f.readlines()
with open(urlfile.format(pro1, '2'), 'r') as f:
    naver_url_balch2 = f.readlines()
with open(urlfile.format(pro1, '3'), 'r') as f:
    naver_url_balch3 = f.readlines()
with open(urlfile.format(pro1, '4'), 'r') as f:
    naver_url_balch4 = f.readlines()


with open(urlfile.format(pro2, '1'), 'r') as f:
    naver_url_vogue1 = f.readlines()
with open(urlfile.format(pro2, '2'), 'r') as f:
    naver_url_vogue2 = f.readlines()

with open(urlfile.format(pro2, '3'), 'r') as f:
    naver_url_vogue3 = f.readlines()
with open(urlfile.format(pro2, '4'), 'r') as f:
    naver_url_vogue4 = f.readlines()


with open(urlfile.format(pro3, '1'), 'r') as f:
    naver_url_semo1 = f.readlines()

with open(urlfile.format(pro3, '2'), 'r') as f:
    naver_url_semo2 = f.readlines()
with open(urlfile.format(pro3, '3'), 'r') as f:
    naver_url_semo3 = f.readlines()
with open(urlfile.format(pro3, '4'), 'r') as f:
    naver_url_semo4 = f.readlines()


with open(urlfile.format(pro4, '1'), 'r') as f:
    naver_url_section1 = f.readlines()
with open(urlfile.format(pro4, '2'), 'r') as f:
    naver_url_section2 = f.readlines()
with open(urlfile.format(pro4, '3'), 'r') as f:
    naver_url_section3 = f.readlines()
with open(urlfile.format(pro4, '4'), 'r') as f:
    naver_url_section4 = f.readlines()


with open(urlfile.format(pro5, '1'), 'r') as f:
    naver_url_show1 = f.readlines()
with open(urlfile.format(pro5, '2'), 'r') as f:
    naver_url_show2 = f.readlines()
with open(urlfile.format(pro5, '3'), 'r') as f:
    naver_url_show3 = f.readlines()

with open(urlfile.format(pro5, '4'), 'r') as f:
    naver_url_show4 = f.readlines()


with open(urlfile.format(pro6, '1'), 'r') as f:
    naver_url_oji1 = f.readlines()
'''
with open(urlfile.format(pro6, '2'), 'r') as f:
    naver_url_oji2 = f.readlines()
with open(urlfile.format(pro6, '3'), 'r') as f:
    naver_url_oji3 = f.readlines()
with open(urlfile.format(pro6, '4'), 'r') as f:
    naver_url_oji4 = f.readlines()

'''
#1qt_balch    
naver_url_list = []
for i in naver_url_balch1:
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
for i in naver_url_balch2:
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
for i in naver_url_balch3:
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
for i in naver_url_balch4:
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


#1qt_vogue    
naver_url_list = []
for i in naver_url_vogue1:
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
for i in naver_url_vogue2:
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
for i in naver_url_vogue3:
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
for i in naver_url_vogue4:
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



#2qt    
naver_url_list = []
for i in naver_url_semo2:
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
for i in naver_url_semo3:
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
for i in naver_url_semo4:
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
for i in naver_url_section1:
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
for i in naver_url_section2:
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
for i in naver_url_section3:
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
for i in naver_url_section4:
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
for i in naver_url_show1:
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
for i in naver_url_show2:
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
for i in naver_url_show3:
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
'''

#2qt_oji    
naver_url_list = []
for i in naver_url_oji2:
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
        
with open(textfile.format(pro6, '2'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)

#3qt    
naver_url_list = []
for i in naver_url_oji3:
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
        
with open(textfile.format(pro6, '3'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)    

#4qt    
naver_url_list = []
for i in naver_url_oji4:
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
        
with open(textfile.format(pro6, '4'), 'w', encoding='utf-8') as f:
    for text in text_list:
        data = text + '\n'
        f.write(data)