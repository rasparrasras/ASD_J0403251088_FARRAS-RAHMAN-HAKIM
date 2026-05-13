#================================================
# Nama : Farras Rahman Hakim
# NIM : J0403251088
# Kelas : TPL B1
#================================================

#================================================
# Latihan 1 : Rekursi Pangkat
#================================================

def pangkat(a, n):
    if n == 0:
        return 1
    else:
        return a * pangkat(a, n - 1)
    
print(pangkat(2, 4)) # Output :16 

# Fungsi pangkat(a, n) menghitung a^n  dengan mengalikan a secara berulang melalui pemanggilan dirinya sendiri (a * pangkat(a, n-1)) hingga n mencapai 0 yang mengembalikan 1 sebagai titik berhenti.