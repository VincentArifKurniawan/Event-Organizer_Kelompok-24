#program utama untuk di-run di terminal
from datetime import date
from dateutil.relativedelta import relativedelta
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
    while True:
        print('Notes: Anda hanya dapat mengadakan acara secepat-cepatnya satu bulan dari sekarang.')
        print('Kapan Anda akan mengadakan acara?')
        dd = int(input('Tanggal = '))
        mm = int(input('Bulan = '))
        yy = int(input('Tahun = '))
        tanggal_acara = date(int(yy), int(mm), int(dd))
        tanggal_limit = date.today() + relativedelta(months=+1)
        if tanggal_acara < tanggal_limit:
            print('Coba lagi.')
        else:
            print('Tanggal valid.')
            break
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
#jenis dan nama acara
namafixpria = []
namafixwanita = []
namafixultah = []
umurfixultah = []
judulfix = []
def namapria():
    nama_pria = input('Nama Pria: ')
    if all(x.isalpha() or x.isspace() for x in nama_pria):
        namafixpria.append(nama_pria)
    else: 
        print('Maaf, nama harus berupa karakter huruf. Coba lagi')
        namapria()
    return namafixpria[-1]

def namawanita():
    nama_wanita = input('Nama Wanita: ')
    if all(x.isalpha() or x.isspace() for x in nama_wanita):
        namafixwanita.append(nama_wanita)
    else: 
        print('Maaf, nama harus berupa karakter huruf. Coba lagi')
        namawanita()
    return namafixwanita[-1]

def namaultah():
    nama_ultah = input('Nama orang yang berulang tahun: ')
    if all(x.isalpha() or x.isspace() for x in nama_ultah):
        namafixultah.append(nama_ultah)
    else:
        print('Maaf, nama harus berupa karakter huruf. Coba lagi')
        namaultah()
    return namafixultah[-1]

def umurultah():
    usia = input('Masukkan usia ulang tahun (angka): ')
    if usia.isnumeric() == False:
        print('Maaf, umur harus berupa karakter angka. Coba lagi')
        umurultah()
    else:
        umurfixultah.append(usia)
    return umurfixultah[-1]

def judulgathering():
    judul = input('Masukkan judul acara Anda: ')
    judulfix.append(judul)
    return judulfix[-1]

def jenis_acara():
    print('='*50)
    print('A. Lamaran')
    print('B. Resepsi Pernikahan')
    print('C. Pesta Ulang Tahun')
    print('D. Ulang Tahun Pernikahan')
    print('E. Gathering')
    try:
        x = input('Acara apa yang akan Anda adakan? ')
        if x.upper() == 'A':
            print('Anda memilih acara lamaran')
            data_klien.append(f'Lamaran {str(namapria())} dan {str(namawanita())}')
        if x.upper() != 'A':
            if x.upper() == 'B':
                print('Anda memilih acara resepsi pernikahan')
                data_klien.append(f'Resepsi pernikahan {str(namapria())} dan {str(namawanita())}')
            if x.upper() != 'B':
                if x.upper() == 'C':
                    print('Anda memilih acara pesta ulang tahun')
                    data_klien.append(f'Pesta ulang tahun {str(namaultah())} ke-{str(umurultah())}')
                if x.upper() != 'C':
                    if x.upper() == 'D':
                        print('Anda memilih acara ulang tahun pernikahan')
                        data_klien.append(f'Pesta ulang tahun pernikahan {str(namapria())} dan {str(namawanita())} yang ke-{str(umurultah())}')
                    if x.upper() != 'D':
                        if x.upper() == 'E':
                            print('Anda memilih acara gathering')
                            data_klien.append(f'Gathering {str(judulgathering())}')
                        else:
                            print('Input tidak valid')
                            jenis_acara()
    except KeyboardInterrupt:
        print('\nMohon tidak menghentikan program secara paksa')
        jenis_acara()
jenis_acara()        
#jumlah undangan
tempatpilihan = booking_data[2]
maksimal = lokasi.lokasi[tempatpilihan]['kapasitas']
print('='*50)
print(f'Kapasitas maksimal gedung yang anda pilih adalah {maksimal}')
diundang = 0
while True:
    undang = int(input('Berapa orang yang Anda undang? '))
    if undang > maksimal:
        print('Mohon maaf, kuota gedung tidak mencukupi.')
    else:
        print(f'Anda mengundang {undang} orang.')
        diundang += undang
        data_klien.append(diundang)
        break
#jenis undangan
import undangan_terbaru as undt
print('='*50)
print('A. Hard Cover')
print('B. Soft Cover')
print('C. Digital')
def pilih_undangan():
    undt.cover()
    undt.verif()
    data_klien.append(undt.cover_dipilih[-1])
pilih_undangan()
#opsi live musik
import band
print('='*50)
print('A. Simple')
print('B. Simple Trio')
print('C. Band')
print('D. Exclusive Band')
print('E. Light Orchestra')
print('F. Big Band')
print('G. Tanpa Live Musik')
def musik():
    band.pilihan()
    band.verif()
    data_klien.append(band.formasi_dipilih[-1])
musik()
#hidangan
import hidangan
print('='*50)
print('A. Prasmanan')
print('B. Catering')
def pesan_makan():
    hidangan.makanan()
    hidangan.verif()
    data_klien.append(hidangan.hidangan_dipilih[-1])
pesan_makan()
#MC
import Modul_MC_Ago as mc
print('='*50)
def pilih_mc():
    mc.main()
    mc.verif()
    data_klien.append(mc.mc_dipilih[-1])
pilih_mc()
#dokumentasi
import Modul_Dok_Wawa as md
print('='*50)
print('A. Fotografi')
print('B. Fotografi dan videografi')
def pilih_dokum():
    md.pilihanD()
    md.verif()
    data_klien.append(md.dokum_dipilih[-1])
pilih_dokum()
#preview output
#contoh akses harga: print(band.formasi[data_klien[5]]['harga'])
biaya_total = 0
print('='*50)
print('='*50)
print('PREVIEW BIAYA PENGADAAN EVENT')
print(f'Nama Klien = {data_klien[0]}')
print(f'Nomor telepon klien = {data_klien[1]}')
print(f'Acara yang diadakan = {data_klien[2]}')
print(f'Waktu pelaksanaan acara = {booking_data[0]}, {booking_data[1]}')
print(f'Lokasi pelaksanaan acara = {booking_data[2]}, biaya = {lokasi.lokasi[booking_data[2]]["harga"]}')
biaya_total += lokasi.lokasi[booking_data[2]]["harga"]
print(f'Jumlah undangan = {data_klien[3]} orang')
if data_klien[4] == 'Digital':
    print(f'Jenis undangan = {data_klien[4]}, biaya = {(undt.undangan[data_klien[4]]["Dengan harga"])}')
    biaya_total += undt.undangan[data_klien[4]]["Dengan harga"]
else:
    print(f'Jenis undangan = {data_klien[4]}, biaya = {(undt.undangan[data_klien[4]]["Dengan harga"])*data_klien[3]}')
    biaya_total += (undt.undangan[data_klien[4]]["Dengan harga"])*data_klien[3]
print(f'Formasi musik = {data_klien[5]}, biaya = {band.formasi[data_klien[5]]["harga"]}')
biaya_total += band.formasi[data_klien[5]]["harga"]
print(f'Tipe hidangan = {data_klien[6]}, biaya = {(hidangan.tipe_hidangan[data_klien[6]]["harga"])*data_klien[3]}')
biaya_total += (hidangan.tipe_hidangan[data_klien[6]]["harga"])*data_klien[3]
print(f'MC = {data_klien[7]}, biaya = {mc.opsi_mc[data_klien[7]]["harga"]}')
biaya_total += mc.opsi_mc[data_klien[7]]["harga"]
print(f'Tipe dokumentasi = {data_klien[8]}, biaya = {md.dokumentasi[data_klien[8]]["harga"]}')
biaya_total += md.dokumentasi[data_klien[8]]["harga"]
print('Estimasi Biaya Total (belum termasuk sewa kostum jika menghendaki:)')
print('Rp',biaya_total,',00')