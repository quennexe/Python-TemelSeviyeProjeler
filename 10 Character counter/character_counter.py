def count_characters(text):
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def main():
    print("🔢 Karakter Sayacı Programına Hoş Geldiniz!")
    text = input("Lütfen bir metin girin: ")

    counts = count_characters(text)

    print(f"\nMetindeki toplam karakter sayısı: {len(text)}")
    print("Her karakterin sayısı:")
    for char, count in sorted(counts.items()):
        if char == " ":
            display_char = "' ' (boşluk)"
        elif char == "\n":
            display_char = "'\\n' (yeni satır)"
        else:
            display_char = char
        print(f"{display_char}: {count}")

if __name__ == "__main__":
    main()
