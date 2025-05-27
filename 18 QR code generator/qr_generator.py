import qrcode

def generate_qr_code(data, filename="qrcode.png"):
    try:
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=5
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill="black", back_color="white")
        img.save(filename)
        print(f"✅ QR kod oluşturuldu ve kaydedildi: {filename}")
    except Exception as e:
        print(f"⚠️ Hata oluştu: {e}")

def main():
    print("🔳 QR Kod Oluşturucuya Hoş Geldiniz!")
    data = input("QR koduna dönüştürülecek veriyi girin: ")
    generate_qr_code(data)

if __name__ == "__main__":
    main()
