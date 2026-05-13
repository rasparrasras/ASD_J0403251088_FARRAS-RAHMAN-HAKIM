#================================================
# Nama : Farras Rahman Hakim
# NIM : J0403251088
# Kelas : TPL B1
#================================================

def merge_sort(data): 
    #Base case: jika data hanya memiliki 1 elemen atau kosong
    if len(data) <= 1: 
        return data 
     
    #Divide: membagi data menjadi 2 bagian
    mid = len(data) // 2 
    left = data[:mid] 
    right = data[mid:] 
     
    #Recursive call: memanggil fungsi merge_sort pada kedua bagian
    left_sorted = merge_sort(left) 
    right_sorted = merge_sort(right) 
     
    return merge(left_sorted, right_sorted) 
 
#Soal: 
#1. Apa yang dimaksud dengan base case? 
#2. Mengapa fungsi memanggil dirinya sendiri? 
#3. Apa tujuan fungsi merge()?

#Jawaban:
#1 Base case adalah kondisi penghentian dalam fungsi rekursif agar fungsi tidak memanggil dirinya terus-menerus.
#2. Karena merge sort menggunakan teknik rekursi dengan strategi divide and conquer yang tujuannya memecah masalah besar menjadi masalah yang lebih kecil sampai mencapai base case.
#3. Fungsi merge bertujuan untuk: Menggabungkan dua list yang sudah terurut menjadi satu list yang tetap terurut.