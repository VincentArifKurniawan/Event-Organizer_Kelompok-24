#MODUL PILIHAN UNDANGAN
undangan = {'Hard Cover':{
    'Undangan anda akan dicetak':'Hard Cover',
    'Dengan harga': 8500},

    'Soft Cover':{
    'Undangan anda akan dicetak':'Soft Cover',
    'Dengan harga': 3000},

    'Digital':{
    'Undangan anda akan dicetak':'Digital',
    'Dengan harga': 100000},
    
}

cover_dipilih = []

def cover():
    try:
        x = input('Pilih jenis cetak isi undangan! (A/B/C) ')
        if x.upper() == 'A':
            print('Undangan berjenis Hard Cover adalah undangan fisik yang\ndapat Anda berikan kepada setiap tamu yang diundang\ndengan bahan hard cover yang awet.\nBiaya percetakan akan dikalikan jumlah undangan.')
            print(undangan['Hard Cover'])
            cover_dipilih.append('Hard Cover')
        if x.upper() != 'A':
            if x.upper() == 'B':
                print('Undangan berjenis Soft Cover adalah undangan fisik yang\ndapat Anda berikan kepada setiap tamu yang diundang\ndengan bahan kertas yang tebal.\nBiaya percetakan akan dikalikan jumlah undangan.')
                print(undangan['Soft Cover'])
                cover_dipilih.append('Soft Cover')
            if x.upper() != 'B':
                if x.upper() == 'C':
                    print('Undangan berjenis Digital adalah undangan digital yang\nberupa link atau file gambar yang dapat Anda berikan\nkepada setiap tamu melalui media komunikasi elektronik.\nBiaya yang tercantum tidak dikenakan biaya percetakan.')
                    print(undangan['Digital'])
                    cover_dipilih.append('Digital')
                else:
                    print('Input tidak valid')
                    cover()
    except KeyboardInterrupt:
        print('\nMohon tidak menghentikan program secara paksa')
        cover()
        

def verif():
    try:
        verifikasi = input('Apakah Anda yakin? (Y/N) ')
        if verifikasi.upper() == 'Y':
            print(f'Jenis undangan yang Anda pilih adalah {cover_dipilih[-1]}')
        if verifikasi.upper() != 'Y':
            if verifikasi.upper() == 'N':
                cover()
                verif()
            else: 
                print('Input tidak valid')
                verif()
    except KeyboardInterrupt:
        print('\nMohon tidak menghentikan program secara paksa')
        verif()