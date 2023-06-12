dokumentasi = {'fotografi' : 1000000,'fotografi dan videografi' : 2000000}

def pilihanD():
    x = input('Pilihan dokumentasi apa yang anda pilih? ')
    if x == 'fotografi':
        print(dokumentasi['fotografi'])
        print('Paket fotografi akan mendapatkan fasilitas pemotretan sebanyak 25 foto serta cetak foto sebanyak 5 lembar yang pastinya menggunakan kualitas kamera dan lebar foto yang memuaskan.')
    if x == 'fotografi dan videografi':
        print(dokumentasi['fotografi dan videografi'])
        print('Paket foto dan videografi merupakan paket gabungan yang memberikan fasilitas pemotretam sebanyak 15 foto, cetak foto sebanyak 3 lembar serta fasilitas 1x take video yang tentunya menggunakan kualitas kamera yang memuaskan.')
    verifikasi = input('Processed? ')
    if verifikasi == 'Y':
        print('lanjut program berikutnya')
    else: pilihanD()
