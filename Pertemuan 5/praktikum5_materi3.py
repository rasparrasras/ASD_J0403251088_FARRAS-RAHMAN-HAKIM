#=========================
#Nama : Farras Rahman Hakim
#NIM : J0403251088
#Kelas : TPL B1
#=========================

#================================================
# Materi rekursif : Menjumlahkan list
#================================================

def jumlah_list(data, index=0):
    return data[index] + jumlah_list(data, index + 1) if index < len(data) else 0

print("======Program Menjumlahkan List======")
data = [1, 2, 3, 4, 5]
print("Hasil Penjumlahan List : ", jumlah_list(data))