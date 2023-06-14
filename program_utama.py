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
data_klien = []
def nama_input():
    try:
        nama = str(input('Masukkan nama Anda = '))
        kondisi1 = all(x.isspace() for x in nama)
        kondisi2 = all(x.isalpha() for x in nama)
        kondisi3 = all(x.isalpha() or x.isspace() for x in nama)
        if kondisi1 == True:
            print('Maaf, nama tidak dapat berupa karakter kosong.')
            nama_input()
        elif kondisi2 == True:
            data_klien.append(nama)
        elif kondisi3 == True:
            data_klien.append(nama)
        else: 
            print('Maaf, nama harus berupa karakter huruf. Coba lagi')
            nama_input()
    except KeyboardInterrupt:
        print('\nMohon tidak menghentikan program secara paksa')
        nama_input()
nama_input()
def no_telp_input():
    try:
        no_telp = input('Masukkan nomor telepon Anda = +62')
        cek_no_telp = no_telp.isnumeric()
        if cek_no_telp == False:
            print('Maaf, nomor telepon harus berupa karakter angka. Coba lagi')
            no_telp_input()
        else: data_klien.append(f'+62{no_telp}')
    except KeyboardInterrupt:
        print('\nMohon tidak menghentikan program secara paksa')
        no_telp_input()
no_telp_input()
print('='*50)
#tanggal acara
def tanggal():
    try:
        while True:
            print('Notes: Anda hanya dapat mengadakan acara secepat-cepatnya satu bulan dari sekarang.')
            print('Kapan Anda akan mengadakan acara? (DD/MM/YYYY)') 
            dd = int(input('Tanggal - Masukkan angka tanggal (DD) = '))
            mm = int(input('Bulan - Masukkan angka bulan (MM) = '))
            yy = int(input('Tahun - Masukkan angka tahun (YYYY) = '))
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
    except KeyboardInterrupt:
        print('\nMohon tidak menghentikan program secara paksa')
        tanggal()
    except ValueError:
        print('\nMohon memberikan input dengan benar')
        tanggal()
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
    kondisi1 = all(x.isspace() for x in nama_pria)
    kondisi2 = all(x.isalpha() for x in nama_pria)
    kondisi3 = all(x.isalpha() or x.isspace() for x in nama_pria)
    if kondisi1 == True:
        print('Maaf, nama tidak dapat berupa karakter kosong.')
        namapria()
    elif kondisi2 == True:
        namafixpria.append(nama_pria)
    elif kondisi3 == True:
        namafixpria.append(nama_pria)
    else: 
        print('Maaf, nama harus berupa karakter huruf. Coba lagi')
        namapria()
    return namafixpria[0]

def namawanita():
    nama_wanita = input('Nama Wanita: ')
    kondisi1 = all(x.isspace() for x in nama_wanita)
    kondisi2 = all(x.isalpha() for x in nama_wanita)
    kondisi3 = all(x.isalpha() or x.isspace() for x in nama_wanita)
    if kondisi1 == True:
        print('Maaf, nama tidak dapat berupa karakter kosong.')
        namawanita()
    elif kondisi2 == True:
        namafixwanita.append(nama_wanita)
    elif kondisi3 == True:
        namafixwanita.append(nama_wanita)
    else: 
        print('Maaf, nama harus berupa karakter huruf. Coba lagi')
        namawanita()
    return namafixwanita[0]

def namaultah():
    nama_ultah = input('Nama orang yang berulang tahun: ')
    kondisi1 = all(x.isspace() for x in nama_ultah)
    kondisi2 = all(x.isalpha() for x in nama_ultah)
    kondisi3 = all(x.isalpha() or x.isspace() for x in nama_ultah)
    if kondisi1 == True:
        print('Maaf, nama tidak dapat berupa karakter kosong.')
        namaultah()
    elif kondisi2 == True:
        namafixultah.append(nama_ultah)
    elif kondisi3 == True:
        namafixultah.append(nama_ultah)
    else:
        print('Maaf, nama harus berupa karakter huruf. Coba lagi')
        namaultah()
    return namafixultah[0]

def umurultah():
    usia = input('Masukkan usia ulang tahun (angka): ')
    if usia.isnumeric() == False:
        print('Maaf, umur harus berupa karakter angka. Coba lagi')
        umurultah()
    else:
        umurfixultah.append(usia)
    return umurfixultah[0]

def judulgathering():
    judul = input('Masukkan judul acara Anda: ')
    kondisi1 = all(x.isspace() for x in judul)
    kondisi2 = all(x.isalpha() for x in judul)
    kondisi3 = all(x.isalnum() or x.isspace() for x in judul)
    if kondisi1 == True:
        print('Maaf, judul tidak dapat berupa karakter kosong.')
        judulgathering()
    elif kondisi2 == True:
        judulfix.append(judul)
    elif kondisi3 == True:
        judulfix.append(judul)
    else: 
        print('Maaf, nama harus berupa karakter huruf. Coba lagi')
        judulgathering()
    return judulfix[0]

def jenis_acara():
    print('='*50)
    print('A. Lamaran')
    print('B. Resepsi Pernikahan')
    print('C. Pesta Ulang Tahun')
    print('D. Ulang Tahun Pernikahan')
    print('E. Gathering')
    try:
        x = input('Acara apa yang akan Anda adakan? (A/B/C/D/E) ')
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
#paket cetak foto
import cetak
print('='*50)
print('A. Paket Kenangan')
print('B. Paket Kenangan Plus')
print('C. Paket Pajangan')
print('D. Paket BigScreen')
print('E. Paket Komplit')
print('F. Tanpa Percetakan')
def pilih_cetak():
    cetak.pilihancetak()
    cetak.verif()
    data_klien.append(cetak.cetak_dipilih[-1])
pilih_cetak()
#preview output
biaya_total = 0
print('='*50)
print('='*50)
print('PREVIEW BIAYA PENGADAAN EVENT')
def preview():
    global biaya_total
    print(f'Nama Klien = {data_klien[0]}')
    print(f'Nomor telepon klien = {data_klien[1]}')
    print(f'Acara yang diadakan = {data_klien[2]}')
    print(f'Waktu pelaksanaan acara = {booking_data[0]}, {booking_data[1]}')
    print(f'Lokasi pelaksanaan acara = {booking_data[2]}, biaya = {"Rp{:,.2f}".format(lokasi.lokasi[booking_data[2]]["harga"])}')
    biaya_total += lokasi.lokasi[booking_data[2]]["harga"]
    print(f'Jumlah undangan = {data_klien[3]} orang')
    if data_klien[4] == 'Digital':
        print(f'Jenis undangan = {data_klien[4]}, biaya = {"Rp{:,.2f}".format(undt.undangan[data_klien[4]]["Dengan harga"])}')
        biaya_total += undt.undangan[data_klien[4]]["Dengan harga"]
    else:
        print(f'Jenis undangan = {data_klien[4]}, biaya = {"Rp{:,.2f}".format((undt.undangan[data_klien[4]]["Dengan harga"])*data_klien[3])}')
        biaya_total += (undt.undangan[data_klien[4]]["Dengan harga"])*data_klien[3]
    print(f'Formasi musik = {data_klien[5]}, biaya = {"Rp{:,.2f}".format(band.formasi[data_klien[5]]["harga"])}')
    biaya_total += band.formasi[data_klien[5]]["harga"]
    print(f'Tipe hidangan = {data_klien[6]}, biaya = {"Rp{:,.2f}".format((hidangan.tipe_hidangan[data_klien[6]]["harga"])*data_klien[3])}')
    biaya_total += (hidangan.tipe_hidangan[data_klien[6]]["harga"])*data_klien[3]
    print(f'MC = {data_klien[7]}, biaya = {"Rp{:,.2f}".format(mc.opsi_mc[data_klien[7]]["harga"])}')
    biaya_total += mc.opsi_mc[data_klien[7]]["harga"]
    print(f'Tipe dokumentasi = {data_klien[8]}, biaya = {"Rp{:,.2f}".format(md.dokumentasi[data_klien[8]]["harga"])}')
    biaya_total += md.dokumentasi[data_klien[8]]["harga"]
    print(f'Percetakan = {data_klien[9]}, biaya = {"Rp{:,.2f}".format(cetak.paket_cetak[data_klien[9]]["harga"])}')
    biaya_total += cetak.paket_cetak[data_klien[9]]["harga"]
    print('Estimasi Biaya Total (belum termasuk sewa kostum jika menghendaki:)')
    print("Rp{:,.2f}".format(biaya_total))
preview()
#contact person
import random
cp = open('contact_person.txt').read().splitlines()
pilih_cp = random.choice(cp)
print(f'Contact Person: {pilih_cp}')
#Nota
def nota():
    global biaya_total
    biaya_total = 0
    print('='*50)
    print('='*50)
    print('NOTA PENGADAAN EVENT')
    preview()
    print('LUNAS')
    print('='*50)
    print('='*50)
#catat output valid
def catat_output():
    with open('output_valid_klien.txt','a') as f:
        print('='*50, file=f)
        print(f'Nama Klien = {data_klien[0]}',file=f)
        print(f'Nomor telepon klien = {data_klien[1]}',file=f)
        print(f'Acara yang diadakan = {data_klien[2]}',file=f)
        print(f'Waktu pelaksanaan acara = {booking_data[0]}, {booking_data[1]}',file=f)
        print(f'Lokasi pelaksanaan acara = {booking_data[2]}',file=f)
        print(f'Jumlah undangan = {data_klien[3]} orang',file=f)
        print(f'Jenis undangan = {data_klien[4]}',file=f)
        print(f'Formasi musik = {data_klien[5]}',file=f)
        print(f'Tipe hidangan = {data_klien[6]}',file=f)
        print(f'MC = {data_klien[7]}',file=f)
        print(f'Tipe dokumentasi = {data_klien[8]}',file=f)
        print('Estimasi Biaya Total:',file=f)
        print("Rp{:,.2f}".format(biaya_total),file=f)
        print('='*50, file=f)
        print('\n',file=f)
#pembayaran
print('Silakan melanjutkan ke pembayaran.')
print('A. BCA')
print('B. Mandiri')
print('C. BNI')
def carabayar():
    try:
        cara_bayar = input('Anda akan membayar melalui bank apa? ')
        if cara_bayar.upper() == 'A':
            print('Nomor rekening bank BCA = 1234567890 a.n. abcdefg')
        if cara_bayar.upper() != 'A':
            if cara_bayar.upper() == 'B':
                print('Nomor rekening bank Mandiri = 1234567890 a.n. abcdefg')
            if cara_bayar.upper() != 'B':
                if cara_bayar.upper() == 'C':
                    print('Nomor rekening bank BNI = 1234567890 a.n. abcdefg')
                else:
                    print('Input tidak valid')
                    carabayar()
    except KeyboardInterrupt:
        print('\nMohon tidak menghentikan program secara paksa')
        carabayar()
carabayar()
import random
kode_otp = random.randrange(100000,999999)
def generate():
    kesempatan = 3
    x = open('otp.txt', 'w')
    tulis = str(kode_otp)
    x.write(tulis)
    x.close()
    print('Mohon perhatikan bahwa kesempatan Anda mengisi kode OTP hanya 3 kali.')
    while kesempatan != 0:
        otp_input = int(input('Masukkan kode OTP = '))
        if otp_input != kode_otp:
            print(f'Coba lagi. Kesempatan Anda {kesempatan - 1} kali.')
            kesempatan -= 1
        else:
            print('Terima kasih! Pembayaran telah terverifikasi.')
            nota()
            catat_output()
            break
    if kesempatan == 0:
        print('Anda gagal verifikasi pembayaran sebanyak 3 kali.\nMohon maaf, pesanan Anda kami anggap tidak valid.')
        with open('booking.txt','r') as baca_datatempat:
            data_ada = baca_datatempat.readlines()
        datahapus = str(booking_data)
        with open('booking.txt','w') as baca_datatempat:
            for baris in data_ada:
                if baris.strip('\n') != datahapus:
                    baca_datatempat.write(baris)
        booking_data.clear()
        data_klien.clear()
generate()