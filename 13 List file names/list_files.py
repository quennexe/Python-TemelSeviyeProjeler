import os

def list_files(directory):
    try:
        files = os.listdir(directory)
        if not files:
            print(f"'{directory}' dizini boş.")
        else:
            print(f"'{directory}' dizinindeki dosya ve klasörler:")
            for f in files:
                print(f"- {f}")
    except FileNotFoundError:
        print(f"⚠️ '{directory}' dizini bulunamadı.")
    except PermissionError:
        print(f"⚠️ '{directory}' dizinine erişim yetkiniz yok.")

def main():
    print("📂 Dosya İsimlerini Listeleme Programına Hoş Geldiniz!")
    directory = input("Lütfen listelemek istediğiniz dizin yolunu girin: ")
    list_files(directory)

if __name__ == "__main__":
    main()
