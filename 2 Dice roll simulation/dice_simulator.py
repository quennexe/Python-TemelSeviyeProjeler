import random

def roll_dice():
    return random.randint(1, 6)

def main():
    print("🎲 Zar Atma Simülasyonuna Hoş Geldiniz!")
    
    while True:
        input("Zar atmak için Enter'a basın...")
        result = roll_dice()
        print(f"Zar sonucu: {result}")
        
        again = input("Tekrar zar atmak ister misiniz? (e/h): ").lower()
        if again != 'e':
            print("Çıkılıyor... 🎲")
            break

if __name__ == "__main__":
    main()
