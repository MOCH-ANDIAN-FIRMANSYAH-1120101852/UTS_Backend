ikan = ['Tuna', 'Hiu', 'Nemo']
ekspor = ['Amerika', 'Asia', 'Eropa']
waktu = ['Biasa', 'Sedang', 'Cepat']

while True:

    print('==== Toko Ikan International ====')

    for i in range(0, len(ikan)):
        print(f'{i+1}.{ikan[i]}')
    pilih = int(input('Silahkan Pilih Ikan : '))

    print('==== ekspor ====')

    for k in range(0, len(ekspor)):
        print(f'{k+1}.{ekspor[k]}')
    tujuan = int(input('Silahkan Pilih ekspor : '))

    print('==== waktu ====')
    
    for l in range(0, len(waktu)):
        print(f'{l+1}.{waktu[l]}')
    tipe = int(input('Silahkan Pilih waktu : '))


    print('====================')

    print(f'Ikan : {ikan[pilih-1]}')
    print(f'ekspor : {ekspor[tujuan-1]}')
    print(f'Kecepatan Expor : {waktu[tipe-1]}')
    print('Sedang Di Proses')
    print('====================')

    lanjut = input('Apakah Mau Beli Ikan Lagi y/n ')
    if lanjut == 'y' or lanjut == 'Y':
        continue
    else:
        break
