import requests
from geopy.geocoders import Nominatim

# geopyの準備　※ユーザー名を入れないとエラーが出る
geolocator = Nominatim(user_agent="test")

weathercode = {
    0 : "晴天",
    1 : "おおむね晴れ、ときどきくもり",
    2 : "おおむね晴れ、ときどきくもり",
    3 : "おおむね晴れ、ときどきくもり",
    45 : "きり",
    48 : "きり",
    51 : "きり雨",
    53 : "きり雨",
    55 : "きり雨",
    56 : "きり雨",
    57 : "きり雨",
    61 : "雨",
    63 : "雨",
    65 : "雨",
    66 : "雨",
    67 : "雨",
    71 : "雪",
    73 : "雪",
    75 : "雪",
    77 : "雪",
    80 : "にわか雨",
    81 : "にわか雨",
    82 : "にわか雨",
    85 : "にわか雪",
    86 : "にわか雪",
    95 : "らい雨",
    96 : "軽いひょうをともなうらい雨",
    99 : "軽いひょうをともなうらい雨",
}

# 地名から緯度と経度の情報を手に入れる
val = input("天気の情報を手に入れたい市区町村名・地名等を入れてください；")

try:
    location = geolocator.geocode(val)
    ido = location.latitude      #緯度
    keido = location.longitude     #経度
except Exception as e:
    print("エラーが発生しました。プログラムを終了します。")
    exit()

weather_api = "https://api.open-meteo.com/v1/forecast?latitude=" + str(ido) + "&longitude=" + str(keido) + "&hourly=temperature_2m,precipitation_probability,weathercode&timezone=Asia%2FTokyo&forecast_days=1&models=best_match"

api_info = requests.get(weather_api)
json_data = api_info.json()

#print(json_data)

weather_ja = []
for i in range(0, len(json_data['hourly']['weathercode'])):
    weather_ja.append(weathercode[json_data['hourly']['weathercode'][i]])

for i in range(0, len(json_data['hourly']['time'])):
    print(json_data['hourly']['time'][i] +
          " 気温：" + str(json_data['hourly']['temperature_2m'][i]) +
          "℃ 降水確率：" + str(json_data['hourly']['precipitation_probability'][i])
          + "％ 天気：" + weather_ja[i])
