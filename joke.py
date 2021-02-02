import requests
from bs4 import BeautifulSoup
from time import sleep
from random import random
def get_joke(page):
    for i in range(page):
        url=f"https://www.qiushibaike.com/text/page/{i+1}/"
        headers={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding":"gzip, deflate, br",
        "Accept-Language":"zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Cookie":'''[Cookie: _xsrf=2|38ea450c|88604c29d52f3b304c1ca6a49355af45|1612148988; _qqq_uuid_="2|1:0|10:1612148989|10:_qqq_uuid_|56:ZTk5ZmVmOThkYTk2ZmNhMTI3MDEzNmUzMjBhYjM0OWU3NDhkNzU1Mw==|308de5b8d697bee86590b0c5f86628c815cf2165b7dbf5c7e75dc1fb89f20e8a"; Hm_lvt_2670efbdd59c7e3ed3749b458cafaa37=1612148989; _ga=GA1.2.796355606.1612148989; _gid=GA1.2.486399004.1612148990; gr_user_id=9886fd68-aa3c-4b57-bbce-8668886651fa; grwng_uid=d00c3b17-00e0-4116-a29a-81ccd4eafa6e; __cur_art_index=6500; ff2672c245bd193c6261e9ab2cd35865_gr_session_id=35c218fb-a64f-4e41-9a35-babd186aeac8; ff2672c245bd193c6261e9ab2cd35865_gr_session_id_35c218fb-a64f-4e41-9a35-babd186aeac8=true; Hm_lpvt_2670efbdd59c7e3ed3749b458cafaa37=1612153354''',
        "Referer":"https://www.qiushibaike.com/text/",
        "Host":"www.qiushibaike.com",
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"
        }
        
        info=requests.get(url,headers=headers)
        soup=BeautifulSoup(info.text,features="lxml")
        with open("joke.txt","a") as f:
            for i,j,k,l,m in zip(soup.find_all("h2"),soup.find_all("div",class_="articleGender"),soup.find_all("div",class_="content"),soup.find_all("span",class_="stats-vote"),soup.find_all("span",class_="stats-comments")):
                author=i.get_text(strip=True)
                if "women" in j["class"][1]:
                    gender="女性"
                else:
                    gender="男性"
                age=j.get_text()
                content=k.get_text(strip=True)
                like=l.get_text(strip=True)
                comments=m.get_text(strip=True)
                f.write(author+" "+gender+" "+age+"岁"+"\n"+content+"\n"+like+comments+"\n\n")
        sleep(2+random())
if __name__ == '__main__':
    get_joke(5)
