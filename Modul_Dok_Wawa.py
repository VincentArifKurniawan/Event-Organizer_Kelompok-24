dokumentasi = {'fotografi' : {'harga':1000000},'fotografi dan videografi' : {'harga': 2000000}}

dokum_dipilih =  []

def pilihanD():
    try:
        x = input('Pilihan dokumentasi apa yang Anda pilih? (A/B) ')
        if x.upper() == 'A':
            print(dokumentasi['fotografi'])
            dokum_dipilih.append('fotografi')
        if x.upper() != 'A':
            if x.upper() == 'B':
                dokum_dipilih.append('fotografi dan videografi')
            else: 
                print('Input tidak valid')
                pilihanD()
    except KeyboardInterrupt:
        print('\nMohon tidak menghentikan program secara paksa')
        pilihanD()

def verif():
    try:
        verifikasi = input('Apakah Anda yakin? (Y/N) ')
        if verifikasi.upper() == 'Y':
            print(f'Dokumentasi yang Anda pilih adalah {dokum_dipilih[-1]}')
        if verifikasi.upper() != 'Y':
            if verifikasi.upper() == 'N':
                pilihanD()
                verif()
            else: 
                print('Input tidak valid')
                verif()
    except KeyboardInterrupt:
        print('\nMohon tidak menghentikan program secara paksa')
        verif()      