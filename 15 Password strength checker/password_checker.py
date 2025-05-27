import re

def check_password_strength(password):
    strength_points = 0

    if len(password) >= 8:
        strength_points += 1
    if re.search(r"[A-Z]", password):
        strength_points += 1
    if re.search(r"[a-z]", password):
        strength_points += 1
    if re.search(r"\d", password):
        strength_points += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength_points += 1

    if strength_points <= 2:
        return "Zayıf"
    elif strength_points == 3 or strength_points == 4:
        return "Orta"
    else:
        return "Güçlü"

def main():
    print("🔐 Şifre Güçlülük Kontrolüne Hoş Geldiniz!")
    password = input("Şifrenizi girin: ")
    strength = check_password_strength(password)
    print(f"Şifre gücü: {strength}")

if __name__ == "__main__":
    main()
