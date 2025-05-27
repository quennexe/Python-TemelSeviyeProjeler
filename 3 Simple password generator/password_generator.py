import random
import string

def generate_password(length=12, use_symbols=True):
    characters = string.ascii_letters + string.digits
    if use_symbols:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("🔐 Basit Şifre Üreticiye Hoş Geldiniz!")

    try:
        length = int(input("Şifre uzunluğunu girin (varsayılan 12): ") or 12)
    except ValueError:
        print("Geçersiz giriş! Varsayılan uzunluk 12 kullanılacak.")
        length = 12

    use_symbols = input("Semboller dahil edilsin mi? (e/h): ").lower() == 'e'

    password = generate_password(length, use_symbols)
    print(f"🔑 Oluşturulan Şifre: {password}")

if __name__ == "__main__":
    main()
