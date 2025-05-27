import requests

def get_weather(city, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric',
        'lang': 'tr'
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        print(f"🌡️ {city.title()} için sıcaklık: {temp}°C, Hava: {desc}")
    else:
        print("❌ Şehir bulunamadı ya da API anahtarınız geçersiz.")

def main():
    print("☁️ Hava Durumu Uygulaması")

    city = input("Şehir ismini girin: ")
    api_key = "YOUR_API_KEY"  # Buraya kendi OpenWeatherMap API anahtarınızı girin

    get_weather(city, api_key)

if __name__ == "__main__":
    main()
