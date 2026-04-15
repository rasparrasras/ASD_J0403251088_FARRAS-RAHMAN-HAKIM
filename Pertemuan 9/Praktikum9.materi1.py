#=========================================
# Nama : Farras Rahman Hakim
# NIM : J0403251088
# Kelas : TPL B1
#=========================================
#Latihan 1 : Membuat Node
#=========================================

#class node digunakan untuk dasar dari tree

class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

#membuat root
root = Node("A") #Membuat Node root dengan data "A"

#menamplkan isi node
print("Data pada root", root.data)
print("Data childkiri root : ", root.left)
print("Data childkanan root : ", root.right)

#Pembahasan :
"""
Pada latihan ini, kita membuat sebuah class Node yang memiliki atribut data, left, dan right. Atribut data digunakan untuk menyimpan nilai dari node, sedangkan left dan right digunakan untuk menyimpan referensi ke child kiri dan child kanan dari node tersebut.
Kita kemudian membuat sebuah node root dengan data "A". Karena kita belum menambahkan child ke node root, maka left dan right dari node root akan bernilai None. Kita juga menampilkan isi dari node root, yang menunjukkan data "A" dan bahwa child kiri dan child kanan masih kosong (None).
"""