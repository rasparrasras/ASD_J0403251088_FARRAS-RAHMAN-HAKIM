#=========================
#Nama : Farras Rahman Hakim
#NIM : J0403251088
#Kelas : TPL B1
#=========================

#================================================
# Materi rekursif : Kombinasi Biner dengan Batas '1' (Pruning)
#================================================

def biner_batas(n, batas, hasil="", jumlah_1=0):
  # Pruning: Jika jumlah_1 sudah melewati batas, stop
  if jumlah_1 > batas:
    return
  
  # Base case: jika string sudah n, print
    if len(hasil) == n:
        print(hasil)
        return
    
    # Rekursif: tambahkan '0' dan '1' ke hasil
    biner_batas(n, batas, hasil + '0', jumlah_1)  #tambahkan '0' tanpa menambah jumlah_1
    biner_batas(n, batas, hasil + '1', jumlah_1 + 1)  #tambahkan '1' dan increment jumlah_1

biner_batas(4, 2) #memanggil fungsi biner_batas dengan n = 4 dan batas = 2 untuk menghasilkan semua kombinasi biner dengan panjang 4 yang memiliki maksimal 2 '1'    