from tkinter import *
from tkinter import messagebox

def create_account():
    username = username_entry.get()
    password = password_entry.get()
    
    # Mengecek apakah kolom sudah terisi semua
    if username == '' or password == '':
        messagebox.showwarning("Peringatan", "Silakan isi semua kolom!")
        return
    
    # Mengecek apakah username sudah terdaftar
    if check_existing_username(username):
        messagebox.showwarning("Peringatan", "Username sudah terdaftar!")
        return
    
    # Menyimpan akun ke dalam file
    with open("Data_Akun.txt", "a") as file:
        file.write(f"{username}:{password}\n")
    
    messagebox.showinfo("Informasi", "Akun berhasil dibuat!")

def login():
    username = username_entry.get()
    password = password_entry.get()
    
    # Mengecek apakah kolom sudah terisi semua
    if username == '' or password == '':
        messagebox.showwarning("Peringatan", "Silakan isi semua kolom!")
        return
    
    # Mengecek kecocokan username dan password
    if check_existing_username(username):
        with open("Data_Akun.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                saved_username, saved_password = line.strip().split(":")
                if saved_username == username and saved_password == password:
                    messagebox.showinfo("Informasi", "Login berhasil!")
                    show_biodata_menu()
                    return
    
    messagebox.showwarning("Peringatan", "Username atau password salah!")

def show_biodata_menu():
    # Menghapus elemen-elemen menu login
    username_label.destroy()
    username_entry.destroy()
    password_label.destroy()
    password_entry.destroy()
    login_button.destroy()
    create_account_button.destroy()
    
    # Menambahkan judul menu biodata klien
    title_label.config(text="Biodata Klien")
    
    # Menambahkan kolom input nama lengkap
    nama_label = Label(window, text="Nama Lengkap:", font=("Helvetica", 12), bg="white")
    nama_label.pack(pady=10)
    
    nama_entry = Entry(window, font=("Helvetica", 12))
    nama_entry.pack(pady=10)
    
    # Menambahkan kolom input alamat tinggal
    alamat_label = Label(window, text="Alamat Tinggal:", font=("Helvetica", 12), bg="white")
    alamat_label.pack(pady=10)
    
    alamat_entry = Entry(window, font=("Helvetica", 12))
    alamat_entry.pack(pady=10)
    
    # Menambahkan kolom input nomor telepon
    telepon_label = Label(window, text="Nomor Telepon:", font=("Helvetica", 12), bg="white")
    telepon_label.pack(pady=10)
    
    telepon_entry = Entry(window, font=("Helvetica", 12))
    telepon_entry.pack(pady=10)
    
    # Menambahkan kolom input username
    username_label = Label(window, text="Username:", font=("Helvetica", 12), bg="white")
    username_label.pack(pady=10)
    
    username_entry = Entry(window, font=("Helvetica", 12))
    username_entry.pack(pady=10)
    
    # Menambahkan kolom input password
    password_label = Label(window, text="Password:", font=("Helvetica", 12), bg="white")
    password_label.pack(pady=10)
    
    password_entry = Entry(window, show="*", font=("Helvetica", 12))
    password_entry.pack(pady=10)
    
    # Menambahkan tombol Simpan
    simpan_button = Button(window, text="Simpan", command=save_biodata, font=("Helvetica", 12))
    simpan_button.pack(pady=10)

def save_biodata():
    nama = nama_entry.get()
    alamat = alamat_entry.get()
    telepon = telepon_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    
    # Mengecek apakah semua kolom terisi
    if nama == '' or alamat == '' or telepon == '' or username == '' or password == '':
        messagebox.showwarning("Peringatan", "Silakan isi semua kolom!")
        return
    
    # Menyimpan biodata ke dalam file
    with open("Biodata_Klien.txt", "a") as file:
        file.write(f"Nama: {nama}\n")
        file.write(f"Alamat: {alamat}\n")
        file.write(f"Telepon: {telepon}\n")
        file.write(f"Username: {username}\n")
        file.write(f"Password: {password}\n")
    
    messagebox.showinfo("Informasi", "Biodata berhasil disimpan!")

def check_existing_username(username):
    with open("Data_Akun.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            saved_username, _ = line.strip().split(":")
            if saved_username == username:
                return True
    return False

# Membuat jendela utama
window = Tk()
window.title("Event Organizer App")
window.geometry("400x400")

# Menambahkan latar belakang gambar
background_image = PhotoImage(file="Background.png")
background_label = Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Menambahkan judul
title_label = Label(window, text="Event Organizer App", font=("Helvetica", 18, "bold"), bg="white")
title_label.pack(pady=20)

# Menambahkan kalimat Just For You!
subtitle_label = Label(window, text="Just For You!", font=("Helvetica", 14), bg="white")
subtitle_label.pack(pady=10)

# Menambahkan kalimat Kelola Event
description_label = Label(window, text="Kelola Event Yang Ingin Anda Adakan Dengan Cepat Dan Mudah, Tanpa Ribet!", font=("Helvetica", 12), bg="white")
description_label.pack(pady=10)

# Menambahkan kalimat Courtesy of Kelompok 24
credit_label = Label(window, text="Courtesy of Kelompok 24 Kelas D Imperiale", font=("Helvetica", 10), bg="white")
credit_label.pack(pady=10)

# Menambahkan form login
login_frame = Frame(window, bg="white")
login_frame.pack(pady=20)

username_label = Label(login_frame, text="Username:", font=("Helvetica", 12), bg="white")
username_label.grid(row=0, column=0, padx=10, pady=10)

username_entry = Entry(login_frame, font=("Helvetica", 12))
username_entry.grid(row=0, column=1, padx=10, pady=10)

password_label = Label(login_frame, text="Password:", font=("Helvetica", 12), bg="white")
password_label.grid(row=1, column=0, padx=10, pady=10)

password_entry = Entry(login_frame, show="*", font=("Helvetica", 12))
password_entry.grid(row=1, column=1, padx=10, pady=10)

login_button = Button(login_frame, text="Login", command=login, font=("Helvetica", 12))
login_button.grid(row=2, column=0, columnspan=2, pady=10)

# Tombol membuat akun
create_account_button = Button(window, text="Buat Akun", command=create_account, font=("Helvetica", 12))
create_account_button.pack(pady=10)

# Menjalankan aplikasi
window.mainloop()
