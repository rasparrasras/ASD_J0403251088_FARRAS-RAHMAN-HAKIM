#=========================
#Nama : Farras Rahman Hakim
#NIM : J0403251088
#Kelas : TPL B1
#=========================

#=========================
#Studi Kasus : Sistem Antrian Layanan Akademik
#Implementasi Queue =>
#Enqueue : Memindahkan pointer rear (nambah data baru dari belakang)
#Dequeue : Memindahkan pointer front (menghapus data dari depan)
#Front -> A-> B > C -> Rear
#=========================

#1) Mendefinisikan Node (Unit dasar linked list)
class Node:
    def __init__(self, nim, nama): #konstruktor
        self.nim = nim#menyimpan NIM mahasiswa
        self.nama = nama#menyimpan nama mahasiswa
        self.next = None #pointer ke node berikutnya

#2) Mendefinisikan queue, terdiri dari front dan rear
class queueAkademik:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        #Ketika queue kosong, front dan rear akan bernilai None
        return self.front is None
    #menambahkan data baru ke bagian belakang (rear)
    def enqueue(self, nim, nama):
        nodeBaru = Node(nim, nama)
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
        else:
            self.rear.next = nodeBaru #rear lama menunjuk ke node baru
            self.rear = nodeBaru #rear baru menjadi node baru

    #mengahpus data paling depan (memberikan layanan akademik)
    def dequeue(self):
        if self.is_empty():
            print("Antrian kosong. Tidak ada mahasiswa yang dilayani")
            return None
       
        #lihat data bagian front, simpan di variabel yang akan dihapus
        node_dilayani = self.front

        #geser pointer front ke next front
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return node_dilayani
    
    def tampilkan(self):
        print("Daftar Antrian Mahasiswa (front -> rear) : ")
        current = self.front
        no = 1
        while current is not None:
            print(f"{no}. {current.nim} - {current.nama}")
            current = current.next
            no += 1

#Program utama

def main():
    
    #instantiasi queue
    q = queueAkademik()

    while True :
        print("====== Sistem Antrian Akdemik =======")
        print("1. Tambah Mahasiswa")
        print("2. Layani MAhasiswa")
        print("3. Lihat Antrian")
        print("4. Keluar")

        pilihan = input("Pilih Menu (1-4): ")

        if pilihan == "1":
            nim = input("Masukkan NIM: ")
            nama = input("Masukkan Nama: ")

            q.enqueue(nim,nama)
            print("Mahasiswa Berhasil ditambahkan")
        
        elif pilihan == "2":
            dilayani = q.dequeue()
            if dilayani is not None:
                print(f"Mahasiswa dilayani {dilayani.nim} - {dilayani.nama}")

        elif pilihan == "3":
            q.tampilkan()

        elif pilihan == "4":
            print("Terimakasih telah menggunakan sistem")
            break

        else:
            print("Pilihan tidak valid")

if __name__ == "__main__":
    main()