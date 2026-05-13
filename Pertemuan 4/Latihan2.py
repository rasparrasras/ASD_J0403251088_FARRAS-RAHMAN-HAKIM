#====================
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

#Queue dengan 2 pointer : front dan rear
class QueueLL:
    def __init__(self):
        self.front = None #node depan
        self.rear = None #node belakang

    def enqueue(self, data):
        #menambah data ke rear
        nodeBaru = Node(data)
        #JIka queue kosong, front dan rear menunjuk ke node Baru
        if self.rear is None: 
            self.front = nodeBaru
            self.rear = nodeBaru
            return
        #Jika queue tidak kosong: rear lama menunjuk ke node baru
        self.rear.next = nodeBaru
        #rear baru menjadi rear
        self.rear = nodeBaru
    
    def dequeue(self):
        #menghapus data dari depan
        #1. Ambil data paling depan
        data_terhapus = self.front.data
        #2. Geser front ke node berikutnya
        self.front = self.front.next
        #3. Jika setelah geser front menjadi None, maka queue kosong, rear juga harus None
        if self.front is None:
            self.rear = None
        return data_terhapus
        print("data yang ingin dihapus tidak ada")

    def tampilkan(self):
        #menampilkan isi queue dari front ke rear
        current =self.front
        print("Front ->", end="->")
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("None - Rear berada di Node terakhir")

#instantiasi objek clas queue
q = QueueLL()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()
