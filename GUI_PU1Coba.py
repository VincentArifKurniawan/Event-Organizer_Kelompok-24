from tkinter import Tk, Label, Entry, Button, StringVar, messagebox
from PIL import ImageTk, Image
from tkinter import LabelFrame

def load_accounts():
    # Fungsi ini akan dipanggil saat aplikasi dimulai untuk memuat akun-akun yang sudah ada dari file txt
    with open("akun.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            username, password = line.strip().split(":")
            accounts[username] = password

def save_accounts():
    # Fungsi ini akan dipanggil saat ada akun baru yang dibuat untuk menyimpan semua akun ke dalam file txt
    with open("akun.txt", "w") as file:
        for username, password in accounts.items():
            file.write(f"{username}:{password}\n")

def login():
    # Fungsi ini akan dipanggil saat tombol Login ditekan
    username = username_entry.get()
    password = password_entry.get()

    if username == "" or password == "":
        messagebox.showwarning("Error", "Username and password are required!")
    elif username in accounts and accounts[username] == password:
        open_biodata_menu()
    else:
        messagebox.showerror("Error", "Invalid username or password!")

def create_account():
    # Fungsi ini akan dipanggil saat tombol Create Account ditekan
    username = username_entry.get()
    password = password_entry.get()

    if username == "" or password == "":
        messagebox.showwarning("Error", "Username and password are required!")
    elif username in accounts:
        messagebox.showerror("Error", "Username already exists!")
    else:
        accounts[username] = password
        save_accounts()  # Menyimpan akun yang baru dibuat
        messagebox.showinfo("Success", "Account created successfully!")

def open_biodata_menu():
    # Fungsi ini akan dipanggil saat login berhasil dan membuka menu biodata
    login_frame.pack_forget()
    biodata_frame.pack()

def save_biodata():
    # Fungsi ini akan dipanggil saat tombol Save ditekan pada menu biodata
    name = name_entry.get()
    phone = phone_entry.get()

    if name == "" or phone == "":
        messagebox.showwarning("Error", "Name and phone are required!")
    else:
        with open("biodata.txt", "a") as file:
            file.write(f"Name: {name}\nPhone: {phone}\n\n")
        messagebox.showinfo("Success", "Biodata saved successfully!")

# Membuat jendela utama
root = Tk()
root.title("Event Organizer")
root.geometry("800x600")

# Memuat gambar latar belakang
background_image = Image.open("TemplateTI.png")
background_image = background_image.resize((800, 600), Image.ANTIALIAS)
bg_image = ImageTk.PhotoImage(background_image)

# Menambahkan label untuk gambar latar belakang
bg_label = Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Menambahkan judul "Event Organizer"
title_label = Label(root, text="Event Organizer", font=("Arial", 20), bg="white")
title_label.pack(pady=10)

# Menambahkan frame untuk menu login
login_frame = LabelFrame(root, text="Login", bg="white")
login_frame.pack(pady=20)

# Menambahkan label dan entry untuk username
username_label = Label(login_frame, text="Username:", bg="white")
username_label.pack()
username_entry = Entry(login_frame)
username_entry.pack()

# Menambahkan label dan entry untuk password
password_label = Label(login_frame, text="Password:", bg="white")
password_label.pack()
password_entry = Entry(login_frame, show="*")
password_entry.pack()

# Menambahkan tombol Login
login_button = Button(login_frame, text="Login", command=login)
login_button.pack()

# Menambahkan tombol Create Account
create_account_button = Button(login_frame, text="Create Account", command=create_account)
create_account_button.pack()

# Menambahkan frame untuk menu biodata
biodata_frame = LabelFrame(root, text="Biodata", bg="white")

# Menambahkan label dan entry untuk nama
name_label = Label(biodata_frame, text="Name:", bg="white")
name_label.pack()
name_entry = Entry(biodata_frame)
name_entry.pack()

# Menambahkan label dan entry untuk telepon
phone_label = Label(biodata_frame, text="Phone:", bg="white")
phone_label.pack()
phone_entry = Entry(biodata_frame)
phone_entry.pack()

# Menambahkan tombol Save
save_button = Button(biodata_frame, text="Save", command=save_biodata)
save_button.pack()

# Menyembunyikan frame biodata
biodata_frame.pack_forget()

# Dictionary untuk menyimpan akun
accounts = {}

# Memuat akun-akun yang sudah ada dari file txt
load_accounts()

# Menjalankan aplikasi
root.mainloop()
