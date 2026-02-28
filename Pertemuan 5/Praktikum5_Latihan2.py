#=========================
#Nama : Farras Rahman Hakim
#NIM : J0403251088
#Kelas : TPL B1
#=========================

#================================================
# Latihan 2 : Tracing Rekursi
#================================================
def countdown(n):
    if n == 0:
        print("Selesai!")
        return
    
    print("Masuk:", n)

    countdown(n - 1)
    print("Keluar:", n)

countdown(3)

# Alasannya: print("Keluar:", n) berada setelah pemanggilan rekursif countdown(n - 1). Artinya baris itu baru dieksekusi setelah semua pemanggilan rekursif di bawahnya selesai. Ini seperti tumpukan (stack