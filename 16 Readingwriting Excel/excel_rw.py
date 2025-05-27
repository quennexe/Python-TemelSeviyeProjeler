import pandas as pd

def read_excel_file(file_path):
    try:
        df = pd.read_excel(file_path)
        print("Excel dosyası başarıyla okundu:")
        print(df)
    except FileNotFoundError:
        print("⚠️ Dosya bulunamadı.")
    except Exception as e:
        print(f"⚠️ Hata: {e}")

def write_excel_file(data, file_path):
    df = pd.DataFrame(data)
    df.to_excel(file_path, index=False)
    print(f"✅ Excel dosyası başarıyla kaydedildi: {file_path}")

def main():
    print("📊 Excel Okuma/Yazma Programına Hoş Geldiniz!\n")

    # Excel dosyası yazalım
    veri = {
        "Ad": ["Ali", "Ayşe", "Mehmet"],
        "Yaş": [25, 30, 22],
        "Şehir": ["İstanbul", "Ankara", "İzmir"]
    }
    write_excel_file(veri, "yeni_veri.xlsx")

    # Yazdığımız dosyayı okuyalım
    read_excel_file("yeni_veri.xlsx")

if __name__ == "__main__":
    main()
