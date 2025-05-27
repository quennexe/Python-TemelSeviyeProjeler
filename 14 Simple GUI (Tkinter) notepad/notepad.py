import tkinter as tk
from tkinter import filedialog, messagebox

def open_file():
    filepath = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if filepath:
        with open(filepath, "r", encoding="utf-8") as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, file.read())
        root.title(f"Not Defteri - {filepath}")

def save_file():
    filepath = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt")])
    if filepath:
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(text_area.get(1.0, tk.END))
        root.title(f"Not Defteri - {filepath}")
        messagebox.showinfo("Başarılı", "Dosya kaydedildi.")

def clear_text():
    text_area.delete(1.0, tk.END)

# Ana pencere
root = tk.Tk()
root.title("Not Defteri")
root.geometry("600x400")

# Menü çubuğu
menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Dosya", menu=file_menu)
file_menu.add_command(label="Aç", command=open_file)
file_menu.add_command(label="Kaydet", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Çık", command=root.quit)

edit_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Düzen", menu=edit_menu)
edit_menu.add_command(label="Temizle", command=clear_text)

# Metin alanı
text_area = tk.Text(root, wrap="word", font=("Arial", 12))
text_area.pack(expand=True, fill="both")

# Başlat
root.mainloop()
