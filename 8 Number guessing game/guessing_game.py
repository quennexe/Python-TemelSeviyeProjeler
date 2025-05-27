import random

def main():
    print("🎯 Sayı Tahmin Oyununa Hoş Geldiniz!")
    number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("1 ile 100 arasında bir sayı tahmin edin: "))
            attempts += 1
            if guess < number:
                print("⬆️ Daha büyük bir sayı deneyin.")
            elif guess > number:
                print("⬇️ Daha küçük bir sayı deneyin.")
            else:
                print(f"🎉 Tebrikler! {attempts} denemede doğru sayıyı buldunuz.")
                break
        except ValueError:
            print("⚠️ Lütfen geçerli bir sayı girin.")

if __name__ == "__main__":
    main()
