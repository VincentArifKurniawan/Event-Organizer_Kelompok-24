import tkinter as tk
from tkinter import messagebox

def create_account():
    username = username_entry.get()
    password = password_entry.get()

    if username == '' or password == '':
        messagebox.showwarning('Peringatan', 'Silakan isi semua kolom!')
    elif check_duplicate_account(username, password):
        messagebox.showwarning('Peringatan', 'Akun dengan username tersebut sudah ada!')
    else:
        with open('Data_Akun.txt', 'a') as file:
            file.write(f'{username},{password}\n')
        messagebox.showinfo('Informasi', 'Akun berhasil dibuat!')

def check_duplicate_account(username, password):
    with open('Data_Akun.txt', 'r') as file:
        accounts = file.readlines()
        for account in accounts:
            saved_username, saved_password = account.strip().split(',')
            if username == saved_username and password == saved_password:
                return True
        return False

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == '' or password == '':
        messagebox.showwarning('Peringatan', 'Silakan isi semua kolom!')
    elif not check_duplicate_account(username, password):
        messagebox.showwarning('Peringatan', 'Username atau password salah!')
    else:
        messagebox.showinfo('Informasi', 'Login berhasil!')
        open_biodata_menu()

def open_biodata_menu():
    login_frame.destroy()
    biodata_frame = tk.Frame(root)
    biodata_frame.pack()

    tk.Label(biodata_frame, text='Biodata Klien', font=('Arial', 16, 'bold')).pack()

    tk.Label(biodata_frame, text='Nama Lengkap:').pack()
    nama_entry = tk.Entry(biodata_frame)
    nama_entry.pack()

    tk.Label(biodata_frame, text='Alamat Tinggal:').pack()
    alamat_entry = tk.Entry(biodata_frame)
    alamat_entry.pack()

    tk.Label(biodata_frame, text='Nomor Telepon:').pack()
    telepon_entry = tk.Entry(biodata_frame)
    telepon_entry.pack()

    tk.Label(biodata_frame, text='Username:').pack()
    username_entry = tk.Entry(biodata_frame)
    username_entry.pack()

    tk.Label(biodata_frame, text='Password:').pack()
    password_entry = tk.Entry(biodata_frame, show='*')
    password_entry.pack()

    def save_biodata():
        nama = nama_entry.get()
        alamat = alamat_entry.get()
        telepon = telepon_entry.get()
        username = username_entry.get()
        password = password_entry.get()

        if nama == '' or alamat == '' or telepon == '' or username == '' or password == '':
            messagebox.showwarning('Peringatan', 'Silakan isi semua kolom!')
        elif not check_duplicate_account(username, password):
            messagebox.showwarning('Peringatan', 'Username atau password tidak valid!')
        else:
            with open('Biodata_Klien.txt', 'a') as file:
                file.write(f'{nama},{alamat},{telepon},{username},{password}\n')
            messagebox.showinfo('Informasi', 'Biodata Klien berhasil disimpan!')

    tk.Button(biodata_frame, text='Simpan', command=save_biodata).pack()

root = tk.Tk()
root.title('Event Organizer App')
root.geometry('500x400')

# Membuat background gambar
background_image = tk.PhotoImage(file='Background.png')
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Membuat frame untuk menu login
login_frame = tk.Frame(root)
login_frame.pack()

# Menampilkan judul dan kalimat pada GUI
tk.Label(login_frame, text='Event Organizer App', font=('Arial', 20, 'bold')).pack()
tk.Label(login_frame, text='Just For You!', font=('Arial', 16)).pack()
tk.Label(login_frame, text='Kelola Event Yang Ingin Anda Adakan\nDengan Cepat Dan Mudah, Tanpa Ribet!', font=('Arial', 12)).pack()
tk.Label(login_frame, text='Courtesy of Kelompok 24 Kelas D Imperiale', font=('Arial', 12)).pack()

# Menampilkan kolom input dan tombol untuk login
tk.Label(login_frame, text='Menu Login', font=('Arial', 14, 'bold')).pack()
tk.Label(login_frame, text='Username:').pack()
username_entry = tk.Entry(login_frame)
username_entry.pack()

tk.Label(login_frame, text='Password:').pack()
password_entry = tk.Entry(login_frame, show='*')
password_entry.pack()

tk.Button(login_frame, text='Buat Akun', command=create_account).pack()
tk.Button(login_frame, text='Login', command=login).pack()

root.mainloop()
