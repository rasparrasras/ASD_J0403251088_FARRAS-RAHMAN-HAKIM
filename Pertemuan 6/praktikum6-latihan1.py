<<<<<<< HEAD
#================================================
# Nama : Farras Rahman Hakim
# NIM : J0403251088
# Kelas : TPL B1
#================================================

def insertion_sort(data): 
    for i in range(1, len(data)): 
        key = data[i] 
        j = i - 1 
         
        while j >= 0 and data[j] > key: 
            data[j + 1] = data[j] 
            j -= 1 
         
        data[j + 1] = key 
     
    return data

#Soal
#1. Mengapa perulangan dimulai dari indeks 1? 
#2. Apa fungsi variabel key? 
#3. Mengapa digunakan while, bukan for? 
#4. Operasi apa yang terjadi di dalam while?

# Jawaban :
#1. Perulangan dimulai dari indeks 1 karena elemen pertama (indeks 0) dianggap sudah berada di posisi yang benar sebagai titik awal perbandingan.
#2. Variabel ini menyimpan nilai elemen yang sedang diproses agar tidak hilang saat angka lain di sebelahnya digeser ke kanan.
#3. While digunakan karena jumlah pergeseran ke kiri tidak pasti; perulangan harus fleksibel dan langsung berhenti begitu posisi yang tepat untuk key ditemukan.
=======
#================================================
# Nama : Farras Rahman Hakim
# NIM : J0403251088
# Kelas : TPL B1
#================================================

def insertion_sort(data): 
    for i in range(1, len(data)): 
        key = data[i] 
        j = i - 1 
         
        while j >= 0 and data[j] > key: 
            data[j + 1] = data[j] 
            j -= 1 
         
        data[j + 1] = key 
     
    return data

#Soal
#1. Mengapa perulangan dimulai dari indeks 1? 
#2. Apa fungsi variabel key? 
#3. Mengapa digunakan while, bukan for? 
#4. Operasi apa yang terjadi di dalam while?

# Jawaban :
#1. Perulangan dimulai dari indeks 1 karena elemen pertama (indeks 0) dianggap sudah berada di posisi yang benar sebagai titik awal perbandingan.
#2. Variabel ini menyimpan nilai elemen yang sedang diproses agar tidak hilang saat angka lain di sebelahnya digeser ke kanan.
#3. While digunakan karena jumlah pergeseran ke kiri tidak pasti; perulangan harus fleksibel dan langsung berhenti begitu posisi yang tepat untuk key ditemukan.
>>>>>>> e8fe87d9f99109e9fc3362abdb3458300d0f17b3
#4. Terjadi proses pergeseran (shifting) elemen yang lebih besar ke arah kanan satu per satu untuk membuka ruang bagi key.