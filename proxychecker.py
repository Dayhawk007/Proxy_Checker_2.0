import random
import requests
from threading import Thread
from bs4 import BeautifulSoup
proxies=open("prox.txt","r")
validproxies=open("valid_proxies.txt","w")
proxies_l=proxies.readlines()
def checker():
    while 1:
        proxy1=random.choice(proxies_l)
        prox_dict={
            "http":f'http://{proxy1[:-1]}',
            "https":f'https://{proxy1[:-1]}'
        }
        try:
            res=requests.get("https://google.com",proxies=prox_dict,timeout=5)
            soup=BeautifulSoup(res.content,features='html.parser')
            for title in soup.find_all('title'):
                if title.text.strip()=="Google":
                    print(proxy1[:-1]+" --"+"Valid "+str(res.elapsed.total_seconds()*1000))
                    validproxies.write(proxy1)
                    validproxies.flush()
        except Exception as e:
            pass
        try:
            proxies_l.remove(proxy1)
        except:
            pass

for _ in range(50):
    x=Thread(target=checker)
    x.start()