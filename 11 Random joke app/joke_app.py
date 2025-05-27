import requests

def get_random_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    try:
        response = requests.get(url)
        response.raise_for_status()
        joke = response.json()
        print(f"🤣 Şaka: {joke['setup']}")
        print(f"😂 Cevap: {joke['punchline']}")
    except requests.RequestException as e:
        print("❌ Şaka alınamadı. İnternet bağlantınızı veya API durumunu kontrol edin.")

def main():
    print("🤣 Rastgele Şaka Uygulamasına Hoş Geldiniz!")
    while True:
        get_random_joke()
        cont = input("\nYeni şaka ister misiniz? (e/h): ").lower()
        if cont != 'e':
            print("👋 Hoşça kalın!")
            break

if __name__ == "__main__":
    main()
