from gtts import gTTS
from playsound import playsound
import os

def convert_text_to_speech(text, lang="tr", filename="output.mp3"):
    try:
        tts = gTTS(text=text, lang=lang)
        tts.save(filename)
        print(f"✅ Ses dosyası kaydedildi: {filename}")
        playsound(filename)
    except Exception as e:
        print(f"⚠️ Hata oluştu: {e}")

def main():
    print("🔊 Yazıyı Sese Dönüştürme Programı (Text to Speech)")
    text = input("Lütfen sese dönüştürmek istediğiniz metni girin: ")
    convert_text_to_speech(text)

if __name__ == "__main__":
    main()
