<<<<<<< HEAD
#=========================================
# Nama : Farras Rahman Hakim
# NIM : J0403251088
# Kelas : TPL B1
#=========================================
#Latihan 3 : Membuat Traversal Preorder
#=========================================

class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

#Fungsi Preorder
def preorder(node):
    if node is not None:
        print(node.data) #Kunjungi node
        preorder(node.left) #Kunjungi subtree kiri
        preorder(node.right) #Kunjungi subtree kanan

#membuat root
root = Node("A") 

#membuat child level 1
root.left = Node("B")
root.right = Node("C")

#membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

#Menjalankan Traversal
print("Hasil Traversal Preorder : ")
preorder(root)

"""
Pada latihan ini, kita membuat sebuah class Node yang memiliki atribut data, left, dan right. Atribut data digunakan untuk menyimpan nilai dari node, sedangkan left dan right digunakan untuk menyimpan referensi ke child kiri dan child kanan dari node tersebut.
Kita kemudian membuat sebuah node root dengan data "A". Kita menambahkan child ke node root, yaitu node "B" sebagai child kiri dan node "C" sebagai child kanan. Selanjutnya, kita menambahkan child ke node "B", yaitu node "D" sebagai child kiri dan node "E" sebagai child kanan.
Kita juga membuat sebuah fungsi preorder yang melakukan traversal preorder pada tree. Traversal preorder mengunj
=======
#=========================================
# Nama : Farras Rahman Hakim
# NIM : J0403251088
# Kelas : TPL B1
#=========================================
#Latihan 3 : Membuat Traversal Preorder
#=========================================

class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

#Fungsi Preorder
def preorder(node):
    if node is not None:
        print(node.data) #Kunjungi node
        preorder(node.left) #Kunjungi subtree kiri
        preorder(node.right) #Kunjungi subtree kanan

#membuat root
root = Node("A") 

#membuat child level 1
root.left = Node("B")
root.right = Node("C")

#membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

#Menjalankan Traversal
print("Hasil Traversal Preorder : ")
preorder(root)

"""
Pada latihan ini, kita membuat sebuah class Node yang memiliki atribut data, left, dan right. Atribut data digunakan untuk menyimpan nilai dari node, sedangkan left dan right digunakan untuk menyimpan referensi ke child kiri dan child kanan dari node tersebut.
Kita kemudian membuat sebuah node root dengan data "A". Kita menambahkan child ke node root, yaitu node "B" sebagai child kiri dan node "C" sebagai child kanan. Selanjutnya, kita menambahkan child ke node "B", yaitu node "D" sebagai child kiri dan node "E" sebagai child kanan.
Kita juga membuat sebuah fungsi preorder yang melakukan traversal preorder pada tree. Traversal preorder mengunj
>>>>>>> e8fe87d9f99109e9fc3362abdb3458300d0f17b3
"""