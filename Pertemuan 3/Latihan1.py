class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" → ")
            temp = temp.next
        print("None")

    def delete_node(self, key):
        temp = self.head

        # Jika yang dihapus adalah head
        if temp and temp.data == key:
            self.head = temp.next
            return True

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            return False

        prev.next = temp.next
        return True


# ======================
# Program Utama
# ======================

ll = LinkedList()

data_list = [3, 7, 12, 19, 25]

for data in data_list:
    ll.append(data)

print("Linked List awal:")
ll.display()

hapus = int(input("Masukkan elemen yang ingin dihapus: "))

if ll.delete_node(hapus):
    print(f"Elemen {hapus} berhasil dihapus.")
else:
    print(f"Elemen {hapus} tidak ditemukan.")

print("Linked List setelah penghapusan:")
ll.display()
