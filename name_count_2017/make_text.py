from bs4 import BeautifulSoup
import urllib.request

#1
f = open('bokmyengawang_url1.txt', 'r')
naver_url = f.readlines()
#print(naver_url)
f.close()


naver_url_list = []
for i in naver_url:
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
                    print(body)
            except:
                pass
    except:
        pass
        
f = open('bokmyengawang_text1.txt', 'w', encoding='utf-8')
for text in text_list:
    data = text + '\n'
    f.write(data)

f.close()



#2
f = open('bokmyengawang_url2.txt', 'r')
naver_url = f.readlines()
#print(naver_url)
f.close()


naver_url_list = []
for i in naver_url:
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
                    print(body)
            except:
                pass
    except:
        pass
        
f = open('bokmyengawang_text2.txt', 'w', encoding='utf-8')
for text in text_list:
    data = text + '\n'
    f.write(data)

f.close()



#3
f = open('bokmyengawang_url3.txt', 'r')
naver_url = f.readlines()
#print(naver_url)
f.close()


naver_url_list = []
for i in naver_url:
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
                    print(body)
            except:
                pass
    except:
        pass
        
f = open('bokmyengawang_text3.txt', 'w', encoding='utf-8')
for text in text_list:
    data = text + '\n'
    f.write(data)

f.close()



#4
f = open('bokmyengawang_url4.txt', 'r')
naver_url = f.readlines()
#print(naver_url)
f.close()


naver_url_list = []
for i in naver_url:
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
                    print(body)
            except:
                pass
    except:
        pass
        
f = open('bokmyengawang_text4.txt', 'w', encoding='utf-8')
for text in text_list:
    data = text + '\n'
    f.write(data)

f.close()


    
