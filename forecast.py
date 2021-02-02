import requests
weather=requests.get("http://wthrcdn.etouch.cn/weather_mini?city="+input("Please enter the city name\n")).json()
try:
    forecast=weather["data"]["forecast"]
except KeyError:
    print("The city doesn't exist")
else:
    for i in range(0,5):
        for j in ["date","high","low","type"]:
            print(forecast[i][j])
