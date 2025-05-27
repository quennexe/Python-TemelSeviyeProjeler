from PIL import Image
import pytesseract
import os

# Eğer Windows'ta iseniz aşağıdaki satırı aktif hale getirin ve yolunuzu ayarlayın:
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def read_text_from_image(image_path):
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img, lang='eng')  # Türkçe için 'tur'
        print("✅ Görselden okunan metin:\n")
        print(text)
    except FileNotFoundError:
        print("⚠️ Görsel bulunamadı.")
    except Exception as e:
        print(f"⚠️ Hata oluştu: {e}")

def main():
    print("🖼️ OCR ile Görselden Metin Okuma")
    image_path = input("Metni okumak istediğiniz görselin yolunu girin: ")
    read_text_from_image(image_path)

if __name__ == "__main__":
    main()
