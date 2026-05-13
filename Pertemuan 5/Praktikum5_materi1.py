#=========================
#Nama : Farras Rahman Hakim
#NIM : J0403251088
#Kelas : TPL B1
#=========================

#================================================
# Materi rekursif : Faktorial
#================================================

def faktorial(n):
    #definisikan base case
    if n <= 1:
        return 1
    #definisikan recursive case
    return n * faktorial(n - 1)

print("======Program Faktorial======")
print("Hasil Faktorial : ", faktorial(100))