#=========================
#Nama : Farras Rahman Hakim
#NIM : J0403251088
#Kelas : TPL B1
#==========================

#================================================
# Latihan 4 : Kombinasi Huruf
#================================================
def kombinasi(n, hasil=""):
    if len(hasil) == n:
        print(hasil)
        return
    
    kombinasi(n, hasil + 'A')
    kombinasi(n, hasil + 'B')

kombinasi(2)

# Total kombinasi = 2^n (2 pilihan huruf per posisi, sebanyak n posisi)
# kombinasi(2) → 2^2 = 4 hasil: AA, AB, BA, BB