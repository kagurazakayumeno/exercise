import requests
url = "https://weibo.com/a/hot/realtime"
headers={"cookie":"SINAGLOBAL=4899164125576.445.1569483786508; _ga=GA1.2.607726785.1606187944; login_sid_t=3e3e878d1281e013809ce14ff53d4554; cross_origin_proto=SSL; _s_tentry=www.google.com.hk; Apache=8691434339720.7295.1607351431470; ULV=1607351431520:25:1:1:8691434339720.7295.1607351431470:1606492754069; WBtopGlobal_register_version=2020120722; SSOLoginState=1607351552; UOR=,,www.google.gg; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW7ZxwLSdOxMS8LmV9Z.F2a5JpX5KMhUgL.FoqX1h54SoeNeh.2dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMcShn71Kq0S054; ALF=1642412668; SCF=At0fdFSPEebAlbxL1MUbqBxNAzXHCrzPa184gIylrAqcF75x737AERgPK4MiFbm5xB9AVDnDy3znXwCP0IFxeUs.; SUB=_2A25NAHauDeRhGeBK41IY9i3LyzWIHXVudO9mrDV8PUNbmtAKLUHMkW9NR5DU7X00CP9vIuBFvTfa-8pg8avt7Jum; WBStorage=8daec78e6a891122|undefined","user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}
realtime=requests.get(url,headers=headers)
realtime.encoding="utf-8"
with open("realtime.html","w",encoding="utf-8") as f:
    f.write(realtime.text)
