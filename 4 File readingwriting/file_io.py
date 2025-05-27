import os

def write_to_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"'{filename}' dosyasına yazıldı.")

def read_from_file(filename):
    if not os.path.exists(filename):
        print("Dosya bulunamadı.")
        return

    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    print(f"'{filename}' içeriği:")
    print("--------------------------")
    print(content)
    print("--------------------------")

def main():
    print("📄 Dosya Okuma ve Yazma Programı")
    
    filename = input("Dosya adını girin (örnek: metin.txt): ")
    content = input("Dosyaya yazmak istediğiniz içeriği girin:\n")

    write_to_file(filename, content)
    print()
    read_from_file(filename)

if __name__ == "__main__":
    main()
