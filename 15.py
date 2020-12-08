import requests
try:
    weather=requests.get('http://wthrcdn.etouch.cn/weather_mini?city='+input('请输入城市名称'))
except:
    print('查询失败')
else:
    data=weather.json()
    data1=data.get("data")
    if data:
        forecast = data['forecast'][0]
        print(forecast.get('date'),forecast.get('high'),forecast.get('low'),forecast.get('type'))
    else:
        print('数据为空！')

