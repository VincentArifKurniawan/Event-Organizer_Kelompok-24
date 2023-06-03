def tampilkan_pilihan_mc():
    print("Berikut adalah Opsi Master Ceremony")
    print("Silakan pilih jumlah MC yang Anda inginkan:")
    print("1. Satu orang MC")
    print("2. Dua orang MC")

def input_jumlah_mc():
    pilihan = input("Masukkan pilihan Anda (1 atau 2): ")
    while pilihan not in ['1', '2']:
        print("Pilihan tidak valid. Mohon masukkan 1 atau 2.")
        pilihan = input("Masukkan pilihan Anda (1 atau 2): ")
    return int(pilihan)

def main():
    tampilkan_pilihan_mc()
    jumlah_mc = input_jumlah_mc()

    if jumlah_mc == 1:
        print("Anda memilih satu orang MC.")
        # Tambahkan kode untuk tindakan yang dilakukan ketika memilih satu orang MC
    else:
        print("Anda memilih dua orang MC.")
        # Tambahkan kode untuk tindakan yang dilakukan ketika memilih dua orang MC

if __name__ == "__main__":
    main()
