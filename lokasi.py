lokasi = {'The Royal Surakarta Heritage':{
    'jenis ruangan':'indoor',
    'kapasitas': 600,
    'alamat': 'Jl.Slamet Riyadi No.6, Kp. Baru, Kec. Pasar Kliwon, Kota Surakarta',
    'harga': 45000000},

    'Pose In Hotel':{
    'jenis ruangan':'indoor',
    'kapasitas': 100,
    'alamat': 'Jl. Mongisidi No.125, Kestalan, Kec. Banjarsari, Kota Surakarta',
    'harga': 16000000},

    'Graha Saba Buana':{
    'jenis ruangan':'indoor',
    'kapasitas': 1000,
    'alamat': 'Jl. Letjen Suprapto No.80-B, Sumber, Kec Banjarsari, Kota Surakarta',
    'harga': 105000000},
    
    'Ramada Suites':{
    'jenis ruangan':'outdoor',
    'kapasitas': 200,
    'alamat': 'Jl, Adi Sucipto No.56, Gatak, Gajahan, Kec.Colomadu, Kab. Karanganyar',
    'harga': 50000000},
    
    'Adhiwangsa Hotel & Convention':{
    'jenis ruangan':'outdoor',
    'kapasitas': 700,
    'alamat': 'Jl. Adi Sucipto No.146, Jajar, Kec. Laweyan, Kota Surakarta',
    'harga': 55000000}
}

tempat_dipilih = []

def pilihan():
    try:
        x = str(input('Pilih di sini (A/B/C/D/E) = '))
        if x.upper() == 'A':
            print(lokasi['The Royal Surakarta Heritage'])
            tempat_dipilih.append('The Royal Surakarta Heritage')
        if x.upper() != 'A':
            if x.upper() == 'B':
                print(lokasi['Pose In Hotel'])
                tempat_dipilih.append('Pose In Hotel')
            if x.upper() != 'B':
                if x.upper() == 'C':
                    print(lokasi['Graha Saba Buana'])
                    tempat_dipilih.append('Graha Saba Buana')
                if x.upper() != 'C':
                    if x.upper() == 'D':
                        print(lokasi['Ramada Suites'])
                        tempat_dipilih.append('Ramada Suites')
                    if x.upper() != 'D':
                        if x.upper() == 'E':
                            print(lokasi['Adhiwangsa Hotel & Convention'])
                            tempat_dipilih.append('Adhiwangsa Hotel & Convention')
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
            print(f'Tempat yang Anda pilih adalah {tempat_dipilih[-1]}')
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