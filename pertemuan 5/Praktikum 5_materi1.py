#=========================
#Nama : Farras Rahman Hakim
#NIM : J0403251088
#Kelas : TPL B1
#=========================

#=========================
#Materi Rekursif : Faktorial
# rekursif case => 3! = 3 x 2 x 1 
# base case 0 berhenti
#=========================

def faktorial(n):
    #base case
    if n == 0:
        return 1
    else:
        return b * faktorial(n-1)
    
print("================Program Menghitung Faktorial===================")
n = int(input("Masukkan nilai n untuk "))