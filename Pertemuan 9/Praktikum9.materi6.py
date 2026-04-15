#=========================================
# Nama : Farras Rahman Hakim
# NIM : J0403251088
# Kelas : TPL B1
#=========================================
#Latihan 6 : struktur organisasi perusahaan
#=========================================

class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

def preorder(node):
    if node is not None:
        print(node.data) #Kunjungi node
        preorder(node.left) #Kunjungi subtree kiri
        preorder(node.right) #Kunjungi subtree kanan

#membuat root
root = Node("Direktur") 

#membuat child level 1
root.left = Node("Manajer A")
root.right = Node("Manajer B")

#membuat child level 2
root.left.left = Node("Staff 1")
root.left.right = Node("Staff 2")
root.right.left = Node("Staff 3")

#Menjalankan Traversal
print("Struktur Organisasi Perusahaan : ")
preorder(root)

#Penjelasan :
"""
Pada latihan ini, kita membuat sebuah class Node yang memiliki atribut data, left, dan right. Atribut data digunakan untuk menyimpan nilai dari node, sedangkan left dan right digunakan untuk menyimpan referensi ke child kiri dan child kanan dari node tersebut.
Kita kemudian membuat sebuah node root dengan data "Direktur". Kita menambahkan child ke node root, yaitu node "Manajer A" sebagai child kiri dan node "Manajer B" sebagai child kanan. Selanjutnya, kita menambahkan child ke node "Manajer A", yaitu node "Staff 1" sebagai child kiri dan node "Staff 2" sebagai child kanan. Kita juga menambahkan child ke node "Manajer B", yaitu node "Staff 3" sebagai child kiri.
"""