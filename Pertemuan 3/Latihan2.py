class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head

    def search(self, key):
        if not self.head:
            return False

        temp = self.head
        while True:
            if temp.data == key:
                return True
            temp = temp.next
            if temp == self.head:
                break

        return False


# ======================
# Program Utama
# ======================

cll = CircularLinkedList()

jumlah = int(input("Masukkan jumlah elemen: "))

for i in range(jumlah):
    data = int(input(f"Masukkan elemen ke-{i+1}: "))
    cll.append(data)

cari = int(input("Masukkan elemen yang ingin dicari: "))

if cll.search(cari):
    print(f"Elemen {cari} ditemukan dalam Circular Linked List.")
else:
    print(f"Elemen {cari} tidak ditemukan dalam Circular Linked List.")
