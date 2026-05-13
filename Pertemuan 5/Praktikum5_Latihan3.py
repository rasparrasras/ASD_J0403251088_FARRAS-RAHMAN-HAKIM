#=========================
#Nama : Farras Rahman Hakim
#NIM : J0403251088
#Kelas : TPL B1
#=========================

#================================================
# Latihan 3 : Mencari Nila Maksimum
#================================================

def maks(data, index=0):
    #base case
    if index == len(data) - 1:
        return data[index]
    
    #recursive case
    max_sisa = maks(data, index + 1)

    if data[index] > max_sisa:
        return data[index]
    else:
        return max_sisa
    
angka = [3, 7, 2, 9, 5]
print("Nilai Maksimum : ", maks(angka))

# Fungsi maks(data, index) mencari nilai terbesar dalam list dengan membandingkan elemen saat ini (data[index]) dengan hasil maksimum dari sisa elemen berikutnya (maks(data, index+1)), dan berhenti ketika index sudah di elemen terakhir (base case) lalu mengembalikan elemen tersebut.