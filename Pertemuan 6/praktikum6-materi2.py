<<<<<<< HEAD
#================================================
# Nama : Farras Rahman Hakim
# NIM : J0403251088
# Kelas : TPL B1
#================================================

#================================================
# Insertion Sort dengan Tracing
#================================================

def insertion_sort(data):
    #melihat data awal
    print("Data Awal: ", data)
    print("="*50)
    #Loop mulai dari data ke 2 *index array ke 1)
    for i in range(1, len(data)):
        
        key = data[i] #simpan nilai yang disisipkan
        j = i - 1 #index elemen terakhir di bagian kiri

        print("Iterasi ke-", i)
        print("Nilai Awal Key: ", key)
        print("Bagian Kiri (belum terurut): ", data[:i])
        print("Bagian Kanan (belum terurut): ", data[i:])

        #Geser
        while j>=0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
        #sisipkan key ke posisi yang benar
        data[j+1] = key

        print("Setelah disipkan : ", data)
        print("-"*50)
        
    return data
#Contoh Penggunaan
angka = [7, 8, 5, 2, 4,6]
=======
#================================================
# Nama : Farras Rahman Hakim
# NIM : J0403251088
# Kelas : TPL B1
#================================================

#================================================
# Insertion Sort dengan Tracing
#================================================

def insertion_sort(data):
    #melihat data awal
    print("Data Awal: ", data)
    print("="*50)
    #Loop mulai dari data ke 2 *index array ke 1)
    for i in range(1, len(data)):
        
        key = data[i] #simpan nilai yang disisipkan
        j = i - 1 #index elemen terakhir di bagian kiri

        print("Iterasi ke-", i)
        print("Nilai Awal Key: ", key)
        print("Bagian Kiri (belum terurut): ", data[:i])
        print("Bagian Kanan (belum terurut): ", data[i:])

        #Geser
        while j>=0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
        #sisipkan key ke posisi yang benar
        data[j+1] = key

        print("Setelah disipkan : ", data)
        print("-"*50)
        
    return data
#Contoh Penggunaan
angka = [7, 8, 5, 2, 4,6]
>>>>>>> e8fe87d9f99109e9fc3362abdb3458300d0f17b3
print("Hasil Sorting: ", insertion_sort(angka))