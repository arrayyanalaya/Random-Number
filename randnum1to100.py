import random

while True:
    angka = [0] * 100
    indeks = 0
    total = 100
    while (indeks < total):
        angka[indeks] = random.randint(1, 100)
        pembanding = 0
        while (pembanding < indeks):
            if (angka[pembanding] == angka[indeks]):
                angka[indeks] = random.randint(1, 100)
                pembanding = -1
            pembanding += 1
        indeks += 1

    print('----- Program angka unik -----')
    pilihan = int(input('1. Mencari angka dalam indeks\n2. Mencari indeks dalam angka\n0. Keluar dari program\nPilihan: '))
    if (pilihan == 1):
        print('')
        indeks = 0
        while (indeks < total):
            print('\t', angka[indeks], end='')
            indeks += 1
        print('\n')
        indeks = int(input('Masukkan indeks: '))
        if indeks <= 0:
            print('Invalid input.')
        else:
            print('Angka:', angka[indeks-1])

    elif (pilihan == 2):
        print('')
        indeks = 0
        while (indeks < total):
            print('\t', angka[indeks], end='')
            indeks += 1
        indeks = 0
        print('\n')
        inputangka = int(input('Masukkan angka: '))
        if (inputangka <= 0):
            print("Angka tersebut tidak ada di indeks")
        else:
            while (indeks < total):
                if (inputangka == angka[indeks]):
                    print('Indeks:', indeks+1)
                indeks += 1

    elif (pilihan == 0):
        exit(input('Tekan enter untuk keluar dari program.'))

    else:
        print('Invalid input.')
    print('------------------------------')