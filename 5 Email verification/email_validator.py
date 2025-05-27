import re

def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None

def main():
    print("📧 E-posta Doğrulama Uygulamasına Hoş Geldiniz!")

    email = input("Lütfen e-posta adresinizi girin: ")

    if is_valid_email(email):
        print("✅ Geçerli bir e-posta adresi!")
    else:
        print("❌ Geçersiz e-posta adresi!")

if __name__ == "__main__":
    main()
