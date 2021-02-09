import requests
import csv
from random import random,randint
from time import sleep
def csdn(page=3):
    url=f"https://www.csdn.net/api/articles?type=more&category=newarticles&shown_offset=161285{randint(1000,9999)}000000"
    for _ in range(page):
        headers={"accept":"application/json, text/javascript, */*; q=0.01",
                "accept-encoding":"gzip, deflate, br",
                "accept-language":"zh-CN,zh;q=0.9",
                "referer":"https://www.csdn.net/nav/newarticles",
                "cookie":"uuid_tt_dd=10_20953333820-1612685472170-224167; Hm_up_6bcd52f51e9b3dce32bec4a3997715ac=%7B%22islogin%22%3A%7B%22value%22%3A%220%22%2C%22scope%22%3A1%7D%2C%22isonline%22%3A%7B%22value%22%3A%220%22%2C%22scope%22%3A1%7D%2C%22isvip%22%3A%7B%22value%22%3A%220%22%2C%22scope%22%3A1%7D%7D; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=6525*1*10_20953333820-1612685472170-224167; _ga=GA1.2.1407468440.1612685473; __gads=ID=d4787159fea807cc-22ff8cb8f6c50061:T=1612685473:RT=1612685473:S=ALNI_MYrY3yllLh4R3rzmVaaCIk2Lw64Ag; ssxmod_itna=eqmxcQqCwxnDgnDzcKRx0I+4DuTxGq0QYTFqDl=7YxA5D8D6DQeGTb2=GCbeC5CDEDpxt+UGOv3tPrahwT4qhRu4GLDmKDyerB+HDxaq0rD74irDDxD3cD7PGmDieC0E5qAQDKxB=DRx07B15DWxDFE2D5ErYFEo5F/h5GDivYRpi8D75Dux0HKBg+DDyvhRxDEGR7l25DvxDkq4vFD4GdZnD3eQxNeD+e+jM4VlDYMDQK3GhxGAQeZQGuPi05ao2cCYD===; log_Id_click=2; dc_session_id=10_1612854122836.333443; dc_sid=b762369ad3f0caf2dafa11de9c5e1663; TY_SESSION_ID=ab5bd3af-d057-4fdb-9ef6-dadfcb7a69d5; c_first_ref=default; c_first_page=https%3A//www.csdn.net/nav/newarticles; c_segment=7; c_page_id=default; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1612710888,1612711240,1612711416,1612854123; dc_tos=qo92i2; log_Id_pv=15; c-login-auto=5; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1612854507; announcement-new=%7B%22isLogin%22%3Afalse%2C%22announcementUrl%22%3A%22https%3A%2F%2Fblog.csdn.net%2Fblogdevteam%2Farticle%2Fdetails%2F112280974%3Futm_source%3Dgonggao_0107%22%2C%22announcementCount%22%3A0%7D; log_Id_view=36",
                "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"}
        csdn=requests.get(url,headers)
        csdn.encoding="utf-8"
        html=csdn.json()
        url=f'''https://www.csdn.net/api/articles?type=more&category=newarticles&shown_offset={html["shown_offset"]}'''
        info=[]
        for i in html["articles"]:
            title=i["title"].strip()
            views=i["views"]
            user_name=i["user_name"]
            info.append((title,views,user_name))
        with open("csdn.csv","a",encoding="utf-8",newline="") as f:
            f_csv=csv.writer(f)
            f_csv.writerows(info)
        sleep(2+random())
if __name__=="__main__":
    csdn()