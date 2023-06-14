tipe_hidangan = {'prasmanan':{'harga':30000},
                 'catering':{'harga':60000}}
#Keterangan: harga tercantum adalah harga per orang (jumlah tamu undangan)

hidangan_dipilih = []

def makanan():
    try:
        x = input('Anda memilih tipe hidangan apa? (A/B) ') 
        if x.upper() == 'A':
            print('Prasmanan adalah tipe hidangan yang disajikan pada suatu meja \nsecara berjajar, dan para tamu dapat mengambil makanan sendiri\ndengan mengantri.')
            print(tipe_hidangan['prasmanan'])
            hidangan_dipilih.append('prasmanan')
        if x.upper() != 'A':
            if x.upper() == 'B':
                print('Catering adalah tipe hidangan yang disajikan melalui jasa waiter/waitress.\nMakanan akan disajikan kepada para tamu dengan diantarkan oleh waiter/waitress\nsesuai dengan porsi yang ditentukan.')
                print(tipe_hidangan['catering'])
                hidangan_dipilih.append('catering')
            else:
                print('Input tidak valid')
                makanan()
    except KeyboardInterrupt:
        print('\nMohon tidak menghentikan program secara paksa')
        makanan()
        
def verif():
    try:
        verifikasi = input('Apakah Anda yakin? (Y/N) ')
        if verifikasi.upper() == 'Y':
            print(f'Tipe hidangan yang Anda pilih adalah {hidangan_dipilih[-1]}')
        if verifikasi.upper() != 'Y':
            if verifikasi.upper() == 'N':
                makanan()
                verif()
            else: 
                print('Input tidak valid')
                verif()
    except KeyboardInterrupt:
        print('\nMohon tidak menghentikan program secara paksa')
        verif()      