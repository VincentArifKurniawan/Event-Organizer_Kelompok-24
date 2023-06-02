#MODUL FORMASI MUSIK/BAND
undangan = {'hard':{
    'Undangan anda akan dicetak':'Hard Cover',
    'Dengan harga': 8500},

    'soft':{
    'Undangan anda akan dicetak':'Soft Cover',
    'Dengan harga': 3000},

    'digital':{
    'Undangan anda akan dicetak':'Digital',
    'Dengan harga': 100000},
    
}
def cover():
    x = input('Pilih jenis cetak isi undangan! ')
    if x == 'A':
        print(undangan['hard'])
    if x == 'B':
        print(undangan['soft'])
    if x == 'C':
        print(undangan['digital'])
    verifikasi = input('Proceed?')
    if verifikasi == 'Y':
     print('Oke') #lanjut ke program berikutnya
    else: cover()


