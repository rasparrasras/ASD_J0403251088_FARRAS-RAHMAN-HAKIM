#=========================================
# Nama : Farras Rahman Hakim
# NIM : J0403251088
# Kelas : TPL B1
#=========================================
# Latihan 1 : BST
#=========================================

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if root is None:
        return Node(data)
    
    if data < root.data:
        root.left= insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)
    return root

#Mengisi Data BST
root = None
data_list = [50, 30, 70, 20, 40, 60, 80]

for data in data_list:
    root = insert(root, data)

print("BST berhasil dibuat:", data_list)

#============================
# Latihan 2 : Traversal Inorder
#============================

def inorder_traversal(root):
    if root is not None:
        inorder_traversal(root.left)
        print(root.data, end=' ')
        inorder_traversal(root.right)

print("Hasil Inorder: ")
inorder_traversal(root)

#============================
# Latihann 3 : Search di BST
#============================

def search(root, key):
    if root is None:
        return False
    
    if root.data == key:
        return True
    if key < root.data:
        return search(root.left, key)
    else:
        return search(root.right, key)
# Uji Pencarian
key= 10

if search(root, key): 
    print("Data ditemukan") 
else: 
    print("Data tidak ditemukan")