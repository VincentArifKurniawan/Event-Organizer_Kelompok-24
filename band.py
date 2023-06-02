#MODUL FORMASI MUSIK/BAND
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
    'harga': 10000000}
}
def pilihan():
    x = input('Formasi apa yang mau dipilih? ')
    if x == 'A':
        print(formasi['simple'])
    if x == 'B':
        print(formasi['simple trio'])
    if x == 'C':
        print(formasi['band'])
    if x == 'D':
        print(formasi['exclusive band'])
    if x == 'E':
        print(formasi['light orchestra'])
    if x == 'F':
        print(formasi['big band'])
    verifikasi = input('Proceed?')
    if verifikasi == 'Y':
     print('Oke') #lanjut ke program berikutnya
    else: pilihan()


