<<<<<<< HEAD
#================================================
# Nama : Farras Rahman Hakim
# NIM : J0403251088
# Kelas : TPL B1
#================================================

#================================================
# Insertion Sort (Ascending)
#================================================

def insertion_sort(data):
    #Loop mulai dari data ke 2 *index array ke 1)
    for i in range(1, len(data)):
        
        key = data[i] #simpan nilai yang disisipkan
        j = i - 1 #index elemen terakhir di bagian kiri

        #Geser
        while j>=0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
        #sisipkan key ke posisi yang benar
        data[j+1] = key
    return data
#Contoh Penggunaan
angka = [7, 8, 5, 2, 4,6]
print("Hasil Sorting: ", insertion_sort(angka))        
=======
#================================================
# Nama : Farras Rahman Hakim
# NIM : J0403251088
# Kelas : TPL B1
#================================================

#================================================
# Insertion Sort (Ascending)
#================================================

def insertion_sort(data):
    #Loop mulai dari data ke 2 *index array ke 1)
    for i in range(1, len(data)):
        
        key = data[i] #simpan nilai yang disisipkan
        j = i - 1 #index elemen terakhir di bagian kiri

        #Geser
        while j>=0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
        #sisipkan key ke posisi yang benar
        data[j+1] = key
    return data
#Contoh Penggunaan
angka = [7, 8, 5, 2, 4,6]
print("Hasil Sorting: ", insertion_sort(angka))        
>>>>>>> e8fe87d9f99109e9fc3362abdb3458300d0f17b3
