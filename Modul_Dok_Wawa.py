dokumentasi = {'fotografi' : 1000000,'fotografi dan videografi' : 2000000}

def pilihanD():
    x = input('Pilihan dokumentasi apa yang anda pilih? ')
    if x == 'fotografi':
        print(dokumentasi['fotografi'])
    if x == 'fotografi dan videografi':
        print(dokumentasi['fotografi dan videografi'])
    verifikasi = input('Processed? ')
    if verifikasi == 'Y':
        print('lanjut program berikutnya')
    else: pilihanD()
