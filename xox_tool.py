import os
import tkinter as tk
from tkinter import messagebox

# Ana pencere
pencere1 = tk.Tk()
pencere1.title("Cone Install Tool (Demo)")
pencere1.geometry("450x200")

# Kullanıcı anlaşma checkbox'ı
checkbox_var1 = tk.BooleanVar()
checkbox1 = tk.Checkbutton(pencere1, text="Anlaşmayı kabul ediyorum", variable=checkbox_var1)
checkbox1.pack(pady=10)

def deal_pass():
    if checkbox_var1.get():
        messagebox.showinfo("Kabul Edildi", "Anlaşma kabul edildi, devam edebilirsiniz.")
        print("Anlaşma kabul edildi")

        # Yeni pencere oluştur (ana pencere değil)
        pencere2 = tk.Toplevel(pencere1)
        pencere2.title("Tool Yükleme Ekranı")
        pencere2.geometry("400x300")
        print("Tool yükleme ekranı açıldı")


        def pass_discord():
                os.system("pkexec dnf install -y https://rpm.discordapp.net/apps/discord/0.0.42/discord-0.0.42-1.x86_64.rpm")
                messagebox.showinfo("Discord Yükleniyor", "İşlem detayları için terminale bakabilirsiniz.")
                print("Discord indirildi ...")


        def pass_chrome():
                os.system("pkexec dnf install -y https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm")
                messagebox.showinfo(f"chrome yükleniyor", "detaylar için terminale bakabilirsiniz.")
                print("chrome indirildi ...")

        #indir butonu chrome için
        button3 = tk.Button(pencere2, text="chrome indir", command=pass_chrome)
        button3.pack()
        # İndir butonu discord için
        button2 = tk.Button(pencere2, text="discord İndir", command=pass_discord)
        button2.pack(pady=10)
    else:
        messagebox.showwarning("Uyarı", "Anlaşma kabul edilmeden uygulamalar kullanılamaz!")

# Devam butonu
button1 = tk.Button(pencere1, text="Devam", command=deal_pass)
button1.pack(pady=10)

# Ana pencere döngüsü
pencere1.mainloop()
