import requests as rq         # url get방식 요청
import csv                    # csv활용
import os                     # 폴더 생성
from datetime import datetime # 시간 변환 요청
API_KEY = os.getenv("API_KEY_W")
city = "seoul"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=kr"
response = rq.get(url)
result = response.json()
# 현재 기온
# 습도 
# 날씨 상태
# 현재 시각
temp = result["main"]["temp"]
humi = result["main"]["humidity"]
weather = result["weather"][0]["description"]
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S") #현재 시각

header = ["current_time","weather","temp","humi"] #csv Header
# 만약, seoul_weather.csv 없으면 만들고
# 있으면 덮어쓰기
csv_exist = os.path.exists("seoul_weather.csv")
# mode
# w:write ,r:read, wb:writebyte ,a:write
with open("seoul_weather.csv", "a") as file:
    writer = csv.writer(file)
    if not csv_exist:
        writer.writerow(header)

    writer.writerow([current_time,weather,temp,humi])
    print("서울 기온 저장 완료")
