import requests
import time
import csv
def movies_poster(code):
    movies = requests.get("http://111.230.211.102:8080/v2/movie/subject/"+code)
    if movies.status_code!=200:
        print("The movie doesn't exist")
    else:
        img_url=movies.json()["img"]
        r = requests.get(img_url)
        with open(f"{code}.jpg", "wb") as f:
            f.write(r.content)
def movies_data():
    with open("data.csv","w+",encoding='utf-8-sig') as f:
        for i in range(1,251,25):
            info=requests.get(f"http://111.230.211.102:8080/v2/movie/top250?start={i}")
            movies_list=info.json()["movies"]
            headers=["id","m_id","name","star","director","quote","img"]
            f_csv = csv.DictWriter(f,headers)
            f_csv.writerows(movies_list)
            time.sleep(3)
def movies_posters():
    for i in range(1,251,25):
        info=requests.get(f"http://111.230.211.102:8080/v2/movie/top250?start={i}")
        for j in range(0,25):
            with open(f"{j+i}.jpg","wb") as f:
                img_url=info.json()["movies"][j]["img"]
                r=requests.get(img_url)
                f.write(r.content)
            time.sleep(3)
