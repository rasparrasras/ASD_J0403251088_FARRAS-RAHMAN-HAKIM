#=========================
#Nama : Farras Rahman Hakim
#NIM : J0403251088
#Kelas : TPL B1
#=========================

#=========================
#Materi Rekursif : Call stack
# Tracing bilangan
# input : 3
# masuk 1 - 2 - 3
#=========================

def hitung(n):
    print(f"Masuk: {n}")
    if n == 0:
        print("Base case tercapai, mulai keluar dari call stack")
        return 
    
    #recursive case
    print(f"masuk {n}")
    hitung(n - 1)
    print(f"Keluar {n}")

# Contoh penggunaan
print("====Hitung Fakorial dengan Tracing====")
hitung(3)