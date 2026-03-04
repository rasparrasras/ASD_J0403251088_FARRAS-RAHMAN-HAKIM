#================================================
# Nama : Farras Rahman Hakim
# NIM : J0403251088
# Kelas : TPL B1
#================================================

#================================================
# Latihan 5 : Melengkapi Kode
#================================================

#Soal 1 : Lengkapi kondisi agar menjadi Ascending
def merge(left, right):
    result = [] #List untuk menyimpan hasil penggabungan
    i = 0
    j = 0

    # Membandingkan elemen dari kedua list 
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Menambahkan sisa elemen jika ada

    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

#Soal 2 : Jelaskan fungsi result.extend().
#Jawaban 2: result.extend() berfungsi untuk menambahkan seluruh sisa elemen list ke dalam result.
#           Saat while berhenti, salah satu list (left atau right) pasti sudah habis.
#           Masih ada sisa elemen di list lainnya yang belum dimasukkan.