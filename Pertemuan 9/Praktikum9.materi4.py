#=========================================
# Nama : Farras Rahman Hakim
# NIM : J0403251088
# Kelas : TPL B1
#=========================================
#Latihan 4 : Membuat Traversal Inorder
#=========================================

class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

#Fungsi Inorder
def inorder(node):
    if node is not None:
        inorder(node.left) #Kunjungi subtree kiri
        print(node.data, end=" ") #Kunjungi node
        inorder(node.right) #Kunjungi subtree kanan

#membuat root
root = Node("A") 

#membuat child level 1
root.left = Node("B")
root.right = Node("C")

#membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

#Menjalankan Traversal
print("Hasil Traversal Inorder : ")
inorder(root)

"""
Pada latihan ini, kita membuat sebuah class Node yang memiliki atribut data, left, dan right. Atribut data digunakan untuk menyimpan nilai dari node, sedangkan left dan right digunakan untuk menyimpan referensi ke child kiri dan child kanan dari node tersebut.
Kita kemudian membuat sebuah node root dengan data "A". Kita menambahkan child ke node root, yaitu node "B" sebagai child kiri dan node "C" sebagai child kanan. Selanjutnya, kita menambahkan child ke node "B", yaitu node "D" sebagai child kiri dan node "E" sebagai child kanan.
Kita juga membuat sebuah fungsi inorder yang melakukan traversal inorder pada tree. Traversal inorder mengunjungi subtree kiri, kemudian node itu sendiri, dan akhirnya subtree kanan.
"""