tipe_hidangan = {'prasmanan':{'harga':30000},
                 'catering':{'harga':60000}}
#Keterangan: harga tercantum adalah harga per orang (jumlah tamu undangan)
def makanan():
    x = input('Anda memilih tipe hidangan apa? ') 
    if x == 'prasmanan':
        print(tipe_hidangan['prasmanan'])
    if x != 'prasmanan':
        if x == 'catering':
            print(tipe_hidangan['catering'])
        else:
            print('Input tidak valid')
            makanan()
        
def verif():
    verifikasi = input('Proceed? (Y/N) ')
    if verifikasi == 'Y':
        print('Oke') #lanjut ke program berikutnya
    if verifikasi != 'Y':
        if verifikasi == 'N':
            makanan()
            verif()
        else: 
            print('Input tidak valid')
            verif()
makanan()
verif()