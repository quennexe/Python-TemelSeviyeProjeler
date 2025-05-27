from datetime import datetime
import time

def show_current_datetime():
    now = datetime.now()
    print("📅 Bugünün tarihi:", now.strftime("%d %B %Y, %A"))
    print("⏰ Şu anki saat:", now.strftime("%H:%M:%S"))

def main():
    print("⏰ Tarih ve Saat Gösterici Programı")
    show_current_datetime()

    refresh = input("\nAnlık saat güncellensin mi? (e/h): ").lower()
    if refresh == 'e':
        try:
            while True:
                print("\r⏳ Anlık saat:", datetime.now().strftime("%H:%M:%S"), end='')
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n🛑 Saat takibi durduruldu.")

if __name__ == "__main__":
    main()
