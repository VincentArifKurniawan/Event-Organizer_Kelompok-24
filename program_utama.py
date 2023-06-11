#program utama untuk di-run di terminal

from datetime import date
TanggalBase = date(1800,1,1)
hari = ["Rabu", "Kamis", "Jumat", "Sabtu", "Minggu", "Senin", "Selasa"]
data_klien = []
booking_data = []
#biodata
print('='*50)
print('EVENT ORGANIZER PROGRAM \nJust For You!')
print('Kelola event yang ingin Anda adakan dengan \ncepat dan mudah, tanpa ribet!')
print('Courtesy of Kelompok 24 Kelas D IMPERIALE')
print('='*50)
def nama_input():
    nama = input('Masukkan nama Anda = ')
    if all(x.isalpha() or x.isspace() for x in nama):
        data_klien.append(nama)
    else: 
        print('Maaf, nama harus berupa karakter huruf. Coba lagi')
        nama_input()
nama_input()
def no_telp_input():
    no_telp = input('Masukkan nomor telepon Anda = +62')
    cek_no_telp = no_telp.isnumeric()
    if cek_no_telp == False:
        print('Maaf, nomor telepon harus berupa karakter angka. Coba lagi')
        no_telp_input()
    else: data_klien.append(f'+62{no_telp}')
no_telp_input()
print('='*50)
#tanggal acara
def tanggal():
    print('Kapan Anda mengadakan acara?')
    dd = int(input('Tanggal = '))
    mm = int(input('Bulan = '))
    yy = int(input('Tahun = '))
    tanggal_acara = date(int(yy), int(mm), int(dd))
    selisih = tanggal_acara - TanggalBase
    index_hari = selisih.days % 7
    hari_acara = hari[index_hari]
    booking_data.append(hari_acara)
    booking_data.append(str(tanggal_acara))
tanggal()
#tempat
import lokasi
print('A. The Royal Surakarta Heritage')
print('B. Pose In Hotel')
print('C. Graha Saba Buana')
print('D. Ramada Suites (outdoor)')
print('E. Adhiwangsa Hotel & Convention (outdoor)')
def pilih_tempat():
    lokasi.pilihan()
    lokasi.verif()
    booking_data.append(lokasi.tempat_dipilih[-1])
pilih_tempat()
print(booking_data)
print('='*50)
#cek tanggal dan tempat
def cek(x):
    baca_datatempat = open('booking.txt','r')
    data_ada = baca_datatempat.read()
    if str(x) in data_ada:
        print('Mohon maaf, tempat dan tanggal tersebut sudah dipesan oleh klien lain. \nMohon coba mengganti tanggal atau tempat')
        ubah = input('A. Tanggal\nB. Tempat\nApa yang ingin Anda ubah? ')
        if ubah.upper() == 'A':
            booking_data.clear()
            tanggal()
            booking_data.append(lokasi.tempat_dipilih[-1])
            cek(booking_data)
        if ubah.upper() != 'A':
            if ubah.upper() == 'B':
                print('A. The Royal Surakarta Heritage')
                print('B. Pose In Hotel')
                print('C. Graha Saba Buana')
                print('D. Ramada Suites (outdoor)')
                print('E. Adhiwangsa Hotel & Convention (outdoor)')
                booking_data.pop()
                pilih_tempat()
                cek(booking_data)
            else: 'Input tidak valid'
    else:
        datatempat = open('booking.txt', 'a')
        datatempat.write(f'\n{str(x)}')
        print('Selamat, tempat yang Anda pesan tersedia! Silakan melanjutkan pesanan Anda.')
cek(booking_data)
