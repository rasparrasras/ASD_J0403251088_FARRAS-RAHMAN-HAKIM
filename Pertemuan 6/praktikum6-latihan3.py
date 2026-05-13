#================================================
# Nama : Farras Rahman Hakim
# NIM : J0403251088
# Kelas : TPL B1
#================================================

#================================================
#Latihan 3
#Buat program dengan menggunakan algoritma insertion sort 
#Tracing dengan  data = [5, 2, 4, 6, 1, 3]
#================================================

#================================================
# Soal
#1. Tuliskan isi list setelah iterasi i = 1. 
#2. Tuliskan isi list setelah iterasi i = 3. 
#3. Berapa kali pergeseran terjadi pada iterasi i = 4?
#================================================

def insertion_sort(data):
    #Loop mulai dari data ke 2 *index array ke 1)
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        
        #Geser elemen yang lebih besar dari key ke kanan
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        
        #Sisipkan key ke posisi yang benar
        data[j + 1] = key
    
    return data

#Jawaban 
#1. Iterasi i = 1 : [2, 5, 4, 6, 1, 3]
#2 Iterasi i = 3 : [2, 4, 5, 6, 1, 3]
#3. Pada Iterasi i = 4, terjadi 4 kali pergeseran