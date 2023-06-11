import tkinter as tk
from tkinter import messagebox

from datetime import date
TanggalBase = date(1800,1,1)
hari = ["Rabu", "Kamis", "Jumat", "Sabtu", "Minggu", "Senin", "Selasa"]
data_klien = []
booking_data = []

def on_submit():
    # Mengambil nilai dari input field
    nama = entry_nama.get()
    no_telp = entry_no_telp.get()
    dd = int(entry_tanggal.get())
    mm = int(entry_bulan.get())
    yy = int(entry_tahun.get())
    tempat = entry_tempat.get()

    if not all(x.isalpha() or x.isspace() for x in nama):
        messagebox.showerror("Error", "Nama harus berupa karakter huruf.")
        return

    if not no_telp.isnumeric():
        messagebox.showerror("Error", "Nomor telepon harus berupa angka.")
        return

    tanggal_acara = date(yy, mm, dd)
    selisih = tanggal_acara - TanggalBase
    index_hari = selisih.days % 7
    hari_acara = hari[index_hari]

    # Memasukkan nilai ke dalam list data_klien dan booking_data
    data_klien.append(nama)
    data_klien.append(f'+62{no_telp}')
    booking_data.append(hari_acara)
    booking_data.append(str(tanggal_acara))
    booking_data.append(tempat)

    # Cek ketersediaan tempat dan tanggal
    if not cek(booking_data):
        messagebox.showinfo("Informasi", "Selamat, tempat yang Anda pesan tersedia! Silakan melanjutkan pesanan Anda.")
        # Melanjutkan proses selanjutnya (misalnya, menyimpan ke file)
        # ...

def cek(booking_data):
    x = booking_data[-1]
    baca_datatempat = open('booking.txt','r')
    data_ada = baca_datatempat.read()
    if str(x) in data_ada:
        messagebox.showerror("Error", "Mohon maaf, tempat dan tanggal tersebut sudah dipesan oleh klien lain. Mohon coba mengganti tanggal atau tempat")
        return False
    else:
        datatempat = open('booking.txt', 'a')
        datatempat.write(f'\n{str(x)}')
        return True

# Membuat jendela utama
window = tk.Tk()
window.title("Event Organizer Program")
window.geometry("400x400")

# Membuat label
label_title = tk.Label(window, text="EVENT ORGANIZER PROGRAM", font=("Arial", 14, "bold"))
label_title.pack(pady=10)

label_nama = tk.Label(window, text="Nama:")
label_nama.pack()

# Membuat input field
entry_nama = tk.Entry(window)
entry_nama.pack()

label_no_telp = tk.Label(window, text="No. Telepon:")
label_no_telp.pack()

entry_no_telp = tk.Entry(window)
entry_no_telp.pack()

label_tanggal = tk.Label(window, text="Tanggal (DD):")
label_tanggal.pack()

entry_tanggal = tk.Entry(window)
entry_tanggal.pack()

label_bulan = tk.Label(window, text="Bulan (MM):")
label_bulan.pack()

entry_bulan = tk.Entry(window)
entry_bulan.pack()

label_tahun = tk.Label(window, text="Tahun (YYYY):")
label_tahun.pack()

entry_tahun = tk.Entry(window)
entry_tahun.pack()

label_tempat = tk.Label(window, text="Tempat:")
label_tempat.pack()

entry_tempat = tk.Entry(window)
entry_tempat.pack()

# Membuat tombol Submit
button_submit = tk.Button(window, text="Submit", command=on_submit)
button_submit.pack(pady=10)

# Memulai loop utama
window.mainloop()
