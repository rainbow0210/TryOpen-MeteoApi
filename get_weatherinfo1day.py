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

def main():
    # 地名から緯度と経度の情報を手に入れる
    val = input("天気の情報を手に入れたい市区町村名・地名等を入れてください；")
    print(geocodeing(val))

def geocodeing(val):
    try:
        location = geolocator.geocode(val)
        ido = location.latitude      #緯度
        keido = location.longitude     #経度

        result = fetch_api(ido, keido)

        return result
    except Exception as e:
        print("エラーが発生しました。プログラムを終了します。")
        exit()

def fetch_api(ido, keido):
    weather_api = "https://api.open-meteo.com/v1/forecast?latitude=" + str(ido) + "&longitude=" + str(keido) + "&daily=weathercode,temperature_2m_max,temperature_2m_min,precipitation_probability_max&timezone=Asia%2FTokyo&forecast_days=1&models=best_match"
    api_info = requests.get(weather_api)
    json_data = api_info.json()

    #print(json_data)

    weather_ja = weathercode[json_data['daily']['weathercode'][0]]

    result = json_data['daily']['time'][0] + " 天気：" + weather_ja + " 最高気温：" + str(json_data['daily']['temperature_2m_max'][0]) + "℃ 最低気温：" + str(json_data['daily']['temperature_2m_min'][0]) + " ℃ 最大降水確率：" + str(json_data['daily']['precipitation_probability_max'][0]) + "％"

    return result

if __name__ == "__main__":
    main()