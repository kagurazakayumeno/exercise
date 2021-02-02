import requests
import csv
import re
from bs4 import BeautifulSoup
from time import sleep
for s in range(1,101):
    url=f"https://nb.lianjia.com/zufang/pg{s}/#contentList"
    headers={"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}
    r=requests.get(url,headers=headers)
    r.encoding="utf-8"
    soup=BeautifulSoup(r.text,features="lxml")
    headers=["title","district","rental","layout","floor","area","direction","href","character"]
    iters=zip(soup.find_all("a",class_="twoline"),soup.find_all("p",class_="content__list--item--des"),soup.find_all("p",class_="content__list--item--bottom oneline"),soup.find_all("span",class_="content__list--item-price"))
    for i,j,k,l in iters:
        title=i.get_text(strip=True)
        href="https://nb.lianjia.com"+i["href"]
        tag=re.sub(r"[-\s]","",j.get_text("|",strip=True))
        if re.findall(r"(\w{3}\|\|\w*)\|\|",tag):
            district=re.findall(r"(\w{3}\|\|\w*)\|\|",tag)[0]
        else:
            continue
        layout=re.findall(r"\d\w\d\w\d\w",tag)[-1]
        floor=re.findall(r"\w{3}\（\w*\）",tag)[0]
        area=re.findall(r"\d{1,3}㎡",tag)[0]
        direction=re.findall(r"\|\/\|([^\d]*)\|\/\|",tag)[-1]
        character=k.get_text("，",strip=True)
        rental=l.get_text(strip=True)
        info=[title,district,rental,layout,floor,area,direction,href,character]
        data=[dict(zip(headers,info))]
        with open("house.csv","a") as f:
            f_csv=csv.DictWriter(f,headers)
            f_csv.writerows(data)
sleep(3)