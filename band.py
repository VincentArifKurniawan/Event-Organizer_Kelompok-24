formasi = {'simple':{
    'alat musik':'Keyboard',
    'penyanyi': 2,
    'harga': 1000000},

    'simple trio':{
    'alat musik':'Drum, Bass, Keyboard',
    'penyanyi': 2,
    'harga': 1500000},

    'band':{
    'alat musik':'Drum, Bass, Keyboard, Gitar',
    'penyanyi': 2,
    'harga': 2500000},
    
    'exclusive band':{
    'alat musik':'Drum, Bass, Keyboard, Gitar, Biola, Saxophone',
    'penyanyi': 2,
    'harga': 3500000},
    
    'light orchestra':{
    'alat musik':'Drum, Bass, Keyboard, Gitar, Saxophone, Cello, Viola, Violin 1, Violin 2',
    'penyanyi': 4,
    'harga': 6000000},
    
    'big band':{
    'alat musik':'Drum, Bass, Keyboard, Gitar, Saxophone, Cello, Viola, Violin 1, Violin 2, Terompet, Trombone, Alto, Saxophone',
    'penyanyi': 4,
    'harga': 10000000},

    'tanpa live musik':{
    'keterangan':'Musik disediakan oleh sound system',
    'harga': 0
    }
}

formasi_dipilih = []

def pilihan():
    try:
        x = input('Formasi apa yang Anda pilih? (A/B/C/D/E/F/G) ')
        if x.upper() == 'A':
            print(formasi['simple'])
            formasi_dipilih.append('simple')
        if x.upper() != 'A':
            if x.upper() == 'B':
                print(formasi['simple trio'])
                formasi_dipilih.append('simple trio')
            if x.upper() != 'B':
                if x.upper() == 'C':
                    print(formasi['band'])
                    formasi_dipilih.append('band')
                if x.upper() != 'C':
                    if x.upper() == 'D':
                        print(formasi['exclusive band'])
                        formasi_dipilih.append('exclusive band')
                    if x.upper() != 'D':    
                        if x.upper() == 'E':
                            print(formasi['light orchestra'])
                            formasi_dipilih.append('light orchestra')
                        if x.upper() != 'E':
                            if x.upper() == 'F':
                                print(formasi['big band'])
                                formasi_dipilih.append('big band')
                            if x.upper() != 'F':
                                if x.upper() == 'G':
                                    print(formasi['tanpa live musik'])
                                    formasi_dipilih.append('tanpa live musik')
                                else:
                                    print('Input tidak valid')
                                    pilihan()
    except KeyboardInterrupt:
        print('\nMohon tidak menghentikan program secara paksa')
        pilihan()

def verif():
    try:
        verifikasi = input('Apakah Anda yakin? (Y/N) ')
        if verifikasi.upper() == 'Y':
            print(f'Formasi yang Anda pilih adalah {formasi_dipilih[-1]}')
        if verifikasi.upper() != 'Y':
            if verifikasi.upper() == 'N':
                pilihan()
                verif()
            else: 
                print('Input tidak valid')
                verif()
    except KeyboardInterrupt:
        print('\nMohon tidak menghentikan program secara paksa')
        verif()      