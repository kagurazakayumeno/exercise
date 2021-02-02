import requests
import csv
from random import random
from bs4 import BeautifulSoup
from time import sleep
def get_python_job(page=100):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36',
        'Connection': 'keep-alive',
    }
    headers1=["title","href","conditions","company_name","company_url","company_financing","welfare","duty"]
    for s in range(page):
        url=f"http://liepin.com/zhaopin/?compkind=&dqs=&pubTime=&pageSize=40&salary=&compTag=&sortFlag=15&degradeFlag=0&compIds=&subIndustry=&jobKind=&industries=&compscale=&key=python&siTag=I-7rQ0e90mv8a37po7dV3Q~fA9rXquZc5IkJpXC-Ycixw&d_sfrom=search_fp&d_ckId=b7e8bb446afb0ac572bbb535c22cc57e&d_curPage=0&d_pageSize=40&d_headId=b7e8bb446afb0ac572bbb535c22cc57e&curPage={s}"
        work=requests.get(url,headers=headers)
        soup= BeautifulSoup(work.text,features="lxml")
        iters=zip(soup.find_all("h3",title=True),soup.find_all("p",class_="condition clearfix"),soup.find_all("p",class_="company-name"),soup.find_all("p",class_="field-financing"),soup.find_all("p",class_="temptation clearfix"))
        for i,j,k,l,m in iters:
            title=i["title"]
            href=i.contents[1]["href"]
            conditions=j["title"]
            company_name=k.get_text(strip=True)
            if k.contents[1].has_attr("href"):
                company_url=k.contents[1]["href"]
            else:
                continue
            company_financing=l.get_text(strip=True)
            welfare=m.get_text("；",strip=True)
            details=requests.get(href,headers=headers)
            soup1=BeautifulSoup(details.text,features="lxml")
            duty=soup1.find("div",class_="content content-word").get_text(strip=True)
            info=[title,href,conditions,company_name,company_url,company_financing,welfare,duty]
            data=[dict(zip(headers1,info))]
            with open("work.csv","a") as f:
                f_csv=csv.DictWriter(f,headers1)
                f_csv.writerows(data)
            sleep(random()+2)
get_python_job()