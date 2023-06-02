# MODUL OPSI UNDANGAN
hard = {
  "Undangan anda akan di cetak ": "hard cover",
  "Dengan harga": 8500
}


soft = {
  "Undagan anda akan dicetak melalui": "soft cover",
  "Dengan Harga" : 3000
}

digital = {
  "Undagan anda akan dicetak digital": "100.000",
}


print('==============')
print('SELAMAT DATANG')
print('Ketik: A untuk Hard Cover')
print('Ketik: B untuk Soft Cover')
print('Ketik: C untuk Digital')
print('==============')


pilih = input('Anda akan mencetak undangan berupa apa? ')
if pilih == 'A':
    print(hard)
if pilih == 'B':
    print(soft)
if pilih == 'C':
    print(digital)
verivikasi = input('Yakin?')
if verivikasi == 'Y':
    print("Terimakasih")
else:
    print("Inputan harus Y/N")


