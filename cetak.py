paket_cetak = {'Paket Kenangan':{
    'isi':'10 lembar foto 8R',
    'harga': 100000},
    
    'Paket Kenangan Plus':{
    'isi':'10 lembar foto 8R + 3 foto dalam pigura kayu 6R',
    'harga': 200000},

    'Paket Pajangan':{
    'isi':'5 lembar foto 8R + 5 lembar foto 12R + 3 foto dalam pigura kayu 6R',
    'harga': 295000},

    'Paket BigScreen':{
    'isi':'5 lembar foto 8R + 5 lembar foto 12R + 3 foto dalam pigura kayu 12R + 1 foto dalam pigura kayu 20R',
    'harga': 425000},

    'Paket Komplit':{
    'isi':'10 lembar foto 8R + 5 lembar foto 12R + 3 foto dalam pigura kayu 6R + 3 foto dalam pigura kayu 12R + 1 foto dalam pigura kayu 20R',
    'harga': 595000},

    'Tanpa Percetakan':{
    'keterangan':'Tidak memilih paket cetak foto',
    'harga': 0    
    }
}

cetak_dipilih = []

def pilihancetak():
    try:
        x = input('Paket percetakan apa yang Anda pilih? (A/B/C/D/E/F) ')
        if x.upper() == 'A':
            print(paket_cetak['Paket Kenangan'])
            cetak_dipilih.append('Paket Kenangan')
        if x.upper() != 'A':
            if x.upper() == 'B':
                print(paket_cetak['Paket Kenangan Plus'])
                cetak_dipilih.append('Paket Kenangan Plus')
            if x.upper() != 'B':
                if x.upper() == 'C':
                    print(paket_cetak['Paket Pajangan'])
                    cetak_dipilih.append('Paket Pajangan')
                if x.upper() != 'C':
                    if x.upper() == 'D':
                        print(paket_cetak['Paket BigScreen'])
                        cetak_dipilih.append('Paket BigScreen')
                    if x.upper() != 'D':    
                        if x.upper() == 'E':
                            print(paket_cetak['Paket Komplit'])
                            cetak_dipilih.append('Paket Komplit')
                        if x.upper() != 'E':
                            if x.upper() == 'F':
                                print(paket_cetak['Tanpa Percetakan'])
                                cetak_dipilih.append('Tanpa Percetakan')
                            else:
                                print('Input tidak valid')
                                pilihancetak()
    except KeyboardInterrupt:
        print('\nMohon tidak menghentikan program secara paksa')
        pilihancetak()

def verif():
    try:
        verifikasi = input('Apakah Anda yakin? (Y/N) ')
        if verifikasi.upper() == 'Y':
            print(f'Paket percetakan yang Anda pilih adalah {cetak_dipilih[-1]}')
        if verifikasi.upper() != 'Y':
            if verifikasi.upper() == 'N':
                pilihancetak()
                verif()
            else: 
                print('Input tidak valid')
                verif()
    except KeyboardInterrupt:
        print('\nMohon tidak menghentikan program secara paksa')
        verif()      