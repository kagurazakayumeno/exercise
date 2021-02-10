import requests
import pymongo
def get_hash(keyword,page):
    for i in range(1,1+page):
        hash_url=f"http://songsearch.kugou.com/song_search_v2?keyword={keyword}&page={i}&pagesize=50"
        headers={"Host":"songsearch.kugou.com",
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"
                }
        try:
            hash=requests.get(hash_url,headers)
        except:
            print("error")
        else:
            for i in hash.json()["data"]["lists"]:
                collection.insert_one(i)
def get_lyrics():
    headers={"Host":"songsearch.kugou.com",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"
            }
    for i in collection.find():
        lyrics_url=f"http://www.kugou.com/yy/index.php?r=play/getdata&hash={i['FileHash']}"
        try:
            req = requests.get(lyrics_url,headers)
        except:
            print("error")
        else:
            content = req.json()
            collection.update_one({'FileHash': i['FileHash']}, {'$set': {'lyrics': content['data']['lyrics']}}, upsert=True)
if __name__=="__main__":
    client=pymongo.MongoClient()
    db=client.kugou
    collection=db.hash
    get_hash("爱",10)
    get_lyrics()
