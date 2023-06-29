opsi_mc = {'1 orang':
             {'harga': 1000000},
             '2 orang':
             {'harga': 2000000},
             'tanpa MC':
             {'harga': 0}
             }

mc_dipilih = []

def tampilkan_pilihan_mc():
    print("Silakan pilih jumlah MC yang Anda inginkan:")
    print("0. Tanpa MC")
    print("1. Satu orang MC")
    print("2. Dua orang MC")

def input_jumlah_mc():
    try:
        pilihan = input("Masukkan pilihan Anda (0/1/2): ")
        while pilihan not in ['0', '1', '2']:
            print("Input tidak valid.")
            pilihan = input("Masukkan pilihan Anda (0/1/2): ")
        return int(pilihan)
    except KeyboardInterrupt:
        print('\nMohon tidak menghentikan program secara paksa')
        input_jumlah_mc()

def verif():
    try:
        verifikasi = input('Apakah Anda yakin? (Y/N) ')
        if verifikasi.upper() == 'Y':
            print(f'Jumlah MC yang Anda pilih adalah {mc_dipilih[-1]}')
        if verifikasi.upper() != 'Y':
            if verifikasi.upper() == 'N':
                main()
                verif()
            else: 
                print('Input tidak valid')
                verif()
    except KeyboardInterrupt:
        print('\nMohon tidak menghentikan program secara paksa')
        verif()      

def main():
    tampilkan_pilihan_mc()
    jumlah_mc = input_jumlah_mc()
    if jumlah_mc == 0:
        print('Anda memilih tanpa MC. Ini dapat Anda pilih apabila\nmenghendaki acara tanpa MC atau sudah ada MC\ndari luar.')
        print(opsi_mc['tanpa MC'])
        mc_dipilih.append('tanpa MC')
    if jumlah_mc != 0:
        if jumlah_mc == 1:
            print("Anda memilih satu orang MC.")
            print(opsi_mc['1 orang'])
            mc_dipilih.append('1 orang')
            # Tambahkan kode untuk tindakan yang dilakukan ketika memilih satu orang MC
        if jumlah_mc != 1:
            if jumlah_mc == 2:
                print("Anda memilih dua orang MC.")
                print(opsi_mc['2 orang'])
                mc_dipilih.append('2 orang')
            else:
                print('Input tidak valid')
                main()
        # Tambahkan kode untuk tindakan yang dilakukan ketika memilih dua orang MC
