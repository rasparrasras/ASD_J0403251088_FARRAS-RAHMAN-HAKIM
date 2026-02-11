#--------------
#Praktikum 1 : Konsep ADT dan File Handling
# Latihan Dasar 1A : Membaca seluruh isi file

#============================

#membuka file dengan mode read
with open('data_mahasiswa.txt', 'r', encoding='utf-8') as file:
    #membaca seluruh isi file
    isi_file = file.read()

    #menampilkan isi file kelayar
    print(isi_file)

    print('===Hasil Read===')
    print('Tipe Data:', type(isi_file))
    print('jumlah baris', isi_file.count('\n')+1)

    #membuka file per baris
    print('===Membaca File Per Baris===')
    jumlah_baris = 0
    with open('data_mahasiswa.txt', 'r', encoding='utf-8') as file:
        #membaca file perbaris
        for baris in file:
            jumlah_baris +=1
            baris = baris.strip() # menghapus spasi dan karakter newline
            print('Baris ke-', jumlah_baris)
            print('isinya :', baris)

#--------------
#Praktikum 1 : Konsep ADT dan File Handling
#Latihan Dasar 2 : Parsing baris menjadi kolom data
#==============================================

with open('data_mahasiswa.txt', 'r', encoding='utf-8') as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(',')
        print('NIM :', nim, '| Nama:', nama, '| Nilai:' , nilai)


#==============================================
#Praktikum 1 : Konsep ADT dan File Handling
#Latihan Dasar 3 : Membaca file dan menyimpan ke list
#==============================================

data_list = [] # list untuk menampung data mahasiswa

with open('data_mahasiswa.txt', 'r', encoding='utf-8') as file:
    for baris in file:
        baris = baris.strip()

        #simpan sebagai list " [Nim, nama, nilai]"
        data_list.append([nim,nama,int(nilai)])

print('====== Data Mahasiswa dalam List=====')
print (data_list)

print('====== Jumlah Record dalam List=====')
print ('Jumlah Record', len(data_list))

print('Contoh Record Pertama: ', data_list[0])

#==============================================
#Praktikum 1 : Konsep ADT dan File Handling
#Latihan Dasar 3 : Membaca file dan menyimpan ke dalam dictionary
#==============================================

data_dict = {}
with open('data_mahasiswa.txt', 'r', encoding='utf-8') as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(',')

        data_dict [nim] = {
            'nama':     nama,
            'nilai': int(nilai)
        }
print('data mahasiswa dalam dictionary')
print(data_dict)