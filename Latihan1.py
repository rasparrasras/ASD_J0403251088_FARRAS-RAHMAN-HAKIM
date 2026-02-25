#=========================
#Implementasi Dasar : Node pada Linked List
#Nama : Farras Rahman Hakim
#NIM : J0403251088
#Kelas : TPL B1
#=========================

#membuat class node (merupakan unit dasar dari linked list)
class Node:
    def __init__(self, data): #konstruktor
        self.data = data #menyimpan niali pada node
        self.next = None #pointer ke node selanjutnya

# 1. Membuat node satu per satu
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

# 2. Menghubungkan node-node tersebut
nodeA.next = nodeB 
nodeB.next = nodeC

# 3. Menentukan node pertama (head)
head = nodeA

# 4. Traversal (menelusuri linked list dari head hingga none)
current = head
while current is not None:
    print(current.data) #menampilkan data pada node saat ini
    current = current.next #pindah ke node selanjutnya

#==========================
#Implementasi Dasar : Linked List : Insert Awal
#===========================

class LinkedList: #class implementasi stack
    def __init__(self):
        self.head = None #node awal kosong

    def insert_awal(self, data):
        #1. Membuat node baru 
        nodeBaru = Node(data) #panggil class node
        #2. node baru menunjuk ke head lama
        nodeBaru.next = self.head
        #3. Menjadikan node baru sebagai head
        self.head = nodeBaru
    
    def hapus_awal(self): #pop dalam stack
        data_terhapus = self.head.data #peek dalam stack
        #menggeser head ke node berikutnya
        self.head = self.head.next
        print ("Node yang dihapus adalah : ", data_terhapus)
     
    def tampilkan(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

print("==========List Baru==========")
ll = LinkedList() #instantiasi objek ke class Linkedlist
ll.insert_awal("X")
ll.insert_awal("Y")
ll.insert_awal("Z")
ll.hapus_awal()
ll.tampilkan()
