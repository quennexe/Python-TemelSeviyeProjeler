def count_words(text):
    words = text.split()
    return len(words)

def main():
    print("🔢 Basit Kelime Sayacı Programına Hoş Geldiniz!")
    text = input("Lütfen bir metin girin: ")
    word_count = count_words(text)
    print(f"Metindeki toplam kelime sayısı: {word_count}")

if __name__ == "__main__":
    main()
