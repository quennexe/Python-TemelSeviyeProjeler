def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            # Kaydırma işlemi (mod 26)
            shifted = (ord(char) - start + shift) % 26 + start
            result += chr(shifted)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    print("🔐 Sezar Şifreleyici (Caesar Cipher)")

    choice = input("Şifrelemek için 'e', çözmek için 'd' yazın: ").lower()
    if choice not in ['e', 'd']:
        print("⚠️ Geçersiz seçim!")
        return

    text = input("Metni girin: ")
    try:
        shift = int(input("Kaydırma miktarını girin (örnek: 3): "))
    except ValueError:
        print("⚠️ Kaydırma sayısı geçerli değil.")
        return

    if choice == 'e':
        encrypted = encrypt(text, shift)
        print(f"Şifrelenmiş metin: {encrypted}")
    else:
        decrypted = decrypt(text, shift)
        print(f"Çözülmüş metin: {decrypted}")

if __name__ == "__main__":
    main()
