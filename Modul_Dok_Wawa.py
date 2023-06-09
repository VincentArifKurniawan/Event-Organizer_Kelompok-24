dokumentasi = {'fotografi' : {'harga':1000000},
               'fotografi dan videografi' : {'harga': 2000000},
               'tanpa dokumentasi':{'harga':0}}

dokum_dipilih =  []

def pilihanD():
    try:
        x = input('Pilihan dokumentasi apa yang Anda pilih? (A/B/C) ')
        if x.upper() == 'A':
            print('Dengan memilih paket fotografi, Anda akan mudah berkoordinasi\ndengan tim dokumentasi kami agar mendapatkan kualitas\nfoto sesuai yang Anda inginkan.')
            print(dokumentasi['fotografi'])
            dokum_dipilih.append('fotografi')
        if x.upper() != 'A':
            if x.upper() == 'B':
                print('Dengan memilih paket fotografi dan videografi, tentunya Anda\ntidak hanya puas dengan hasil foto dari tim dokumentasi kami,\ntapi tim dokumentasi kami juga akan memfasilitasi Anda\ndengan pembuatan video berkualitas tinggi.')
                print(dokumentasi['fotografi dan videografi'])
                dokum_dipilih.append('fotografi dan videografi')
            if x.upper() != 'B':
                if x.upper() == 'C':
                    print('Opsi tanpa dokumentasi dapat Anda pilih\napabila menghendaki tidak adanya tim dokumentasi dari pihak EO\nataupun jika Anda memiliki tim dokumentasi tersendiri.')
                    print(dokumentasi['tanpa dokumentasi'])
                    dokum_dipilih.append('tanpa dokumentasi')
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