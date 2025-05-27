import requests

def fetch_random_user():
    try:
        url = "https://randomuser.me/api/"
        response = requests.get(url)
        response.raise_for_status()  # Hata varsa tetikler
        data = response.json()
        
        user = data['results'][0]
        name = user['name']
        location = user['location']
        email = user['email']

        print("🧑 Rastgele Kullanıcı Bilgisi:")
        print(f"Ad: {name['first']} {name['last']}")
        print(f"E-posta: {email}")
        print(f"Ülke: {location['country']}")
        
    except requests.exceptions.RequestException as e:
        print(f"⚠️ API isteği sırasında hata oluştu: {e}")
    except Exception as e:
        print(f"⚠️ Veri işleme hatası: {e}")

def main():
    print("🌐 Basit API'den Veri Çekme Uygulaması")
    fetch_random_user()

if __name__ == "__main__":
    main()
