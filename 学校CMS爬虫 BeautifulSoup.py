from bs4 import BeautifulSoup
import requests
from threading import Thread
url = ["http://www.yuying.org.cn/",]
txt = open('1.txt', 'w',encoding='utf-8')
def get_url(i):
        res = requests.get(i)
        res = BeautifulSoup(res.text, "html.parser")
        for link in res.find_all('a'):
            this_url = link.get('href')
            if this_url != None:
                url.append("http://www.yuying.org.cn/"+this_url)
                
        
def get_content(url):
    res = requests.get(url)
    res = BeautifulSoup(res.text, "html.parser")
    for p in res.find_all("p"):
        if p.string != None and p.string != "":
            print(p.string)
            txt.write(p.string)


while True:
    t1 = [Thread(target=get_url, args=(url,)) for url in url]
    for i in t1:
        i.start()
        t2 = [Thread(target=get_content, args=(i,)) for i in url]
        for i in t2:
            i.start()





    
        
