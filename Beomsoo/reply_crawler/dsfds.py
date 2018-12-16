import urllib.request
from bs4 import BeautifulSoup
data = ['https://entertain.naver.com/read?oid=382&aid=0000577136']
for u in data:
    with urllib.request.urlopen(u) as url:
        doc = url.read()
        soup = BeautifulSoup(doc, "html.parser")
        reply_count = soup.find_all("span", class_ = "u_cbox_count")
        print(reply_count)