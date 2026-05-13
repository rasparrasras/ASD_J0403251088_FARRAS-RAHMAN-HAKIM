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
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

    def merge(self, list2):
        merged_list = LinkedList()

        temp = self.head
        while temp:
            merged_list.append(temp.data)
            temp = temp.next

        temp = list2.head
        while temp:
            merged_list.append(temp.data)
            temp = temp.next

        return merged_list


# ======================
# Program Utama
# ======================

list1 = LinkedList()
list2 = LinkedList()

input1 = input("Masukkan elemen untuk Linked List 1: ")
input2 = input("Masukkan elemen untuk Linked List 2: ")

data1 = [int(x.strip()) for x in input1.split(",")]
data2 = [int(x.strip()) for x in input2.split(",")]

for num in data1:
    list1.append(num)

for num in data2:
    list2.append(num)

print("Linked List 1:", end=" ")
list1.display()

print("Linked List 2:", end=" ")
list2.display()

hasil = list1.merge(list2)

print("Linked List setelah digabungkan:", end=" ")
hasil.display()
