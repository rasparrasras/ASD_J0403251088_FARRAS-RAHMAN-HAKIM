# ==============================================================================
# UJIAN TENGAH PRAKTIKUM - ALGORITMA & STRUKTUR DATA (TPL2106)
# Nama    : Farras Rahman Hakim
# NIM     : J0403251088
# Kelas   : TPL B/P1
# ==============================================================================

# ==============================================================================
# LOGIKA INTI - ALGORITMA & STRUKTUR DATA
# ==============================================================================

# 1. FILE HANDLING & DICTIONARY
def muat_data_buku(nama_file):
    database_buku = {} # Wadah utama untuk menyimpan data secara efisien
    try:
        # Membuka file eksternal dengan mode 'r' (read/baca)
        with open(nama_file, 'r', encoding='utf-8') as f:
            for line in f:
                # Memecah tiap baris berdasarkan tanda koma (CSV format)
                # .strip() digunakan untuk membuang spasi atau enter di ujung teks
                data = line.strip().split(',')
                if len(data) == 3:
                    kode, judul, harga = data
                    # Memasukkan data ke Dictionary: Kode sebagai KEY (harus unik)
                    # Judul dan Harga sebagai VALUE dalam bentuk nested dictionary
                    database_buku[kode] = {"judul": judul, "harga": int(harga)}
    except FileNotFoundError:
        print(f"Peringatan: File {nama_file} belum dibuat.")
    except Exception as e:
        print(f"Kesalahan sistem: {e}")
    return database_buku

# 2. LINKED LIST - MANAJEMEN PROMOSI
class Node:
    """Representasi elemen tunggal dalam Linked List"""
    def __init__(self, judul):
        self.judul = judul # Menyimpan data utama (Judul Buku)
        self.next = None  # Pointer/Penunjuk ke alamat node selanjutnya

class LinkedListPromosi:
    def __init__(self):
        self.head = None # Head adalah pintu masuk utama ke list

    def tambah_buku_promosi(self, judul):
        """Metode untuk menambahkan data baru ke posisi paling akhir (Append)"""
        new_node = Node(judul)
        if not self.head:      # Jika list masih kosong, node baru jadi head
            self.head = new_node
        else:
            current = self.head
            # Melakukan traversal (penelusuran) sampai menemukan node terakhir
            while current.next:
                current = current.next
            # Menghubungkan node terakhir yang lama ke node yang baru
            current.next = new_node
        print(f"Sukses: '{judul}' masuk daftar promosi.")

    def tampilkan_promosi(self):
        """Melintasi list dari awal hingga akhir untuk mencetak isinya"""
        print("\n--- DAFTAR PROMOSI ---")
        if not self.head:
            print("Belum ada buku promosi.")
            return
        current = self.head
        while current:
            print(f"- {current.judul}")
            current = current.next # Berpindah ke node berikutnya

# 3. QUEUE - ANTREAN KASIR

class AntreanKasir:
    def __init__(self):
        self.antrean = [] # Menggunakan list Python sebagai struktur dasar Queue

    def tampilkan_status_antrean(self):
        """Menampilkan urutan pelanggan yang masih menunggu"""
        if self.antrean:
            print(f"Status Antrean: {' <- '.join(self.antrean)}")
        else:
            print("Status Antrean: Kosong")

    def tambah_antrean(self, nama_pelanggan):
        """Konsep ENQUEUE: Menambahkan elemen ke barisan paling belakang"""
        self.antrean.append(nama_pelanggan)
        print(f"\n[Masuk] Pelanggan '{nama_pelanggan}' bergabung di antrean.")
        self.tampilkan_status_antrean()

    def layani_pelanggan(self):
        """Konsep DEQUEUE: Mengambil elemen dari barisan paling depan (FIFO)"""
        if self.antrean:
            # pop(0) memastikan data yang pertama kali masuk adalah yang pertama keluar
            pelanggan = self.antrean.pop(0)
            print(f"\n[Melayani] Pelanggan '{pelanggan}' sedang diproses.")
            self.tampilkan_status_antrean()
        else:
            print("\n[Peringatan] Tidak ada antrean yang bisa dilayani.")

# 4. SORTING - LAPORAN TRANSAKSI

def urutkan_transaksi(list_harga):

    n = len(list_harga)
    for i in range(1, n): # Dimulai dari elemen kedua (index 1)
        key = list_harga[i] # Elemen yang sedang 'dipegang' untuk dibandingkan
        j = i - 1
        # Menggeser elemen yang lebih besar ke kanan
        while j >= 0 and key < list_harga[j]:
            list_harga[j + 1] = list_harga[j]
            j -= 1
        # Menempatkan elemen 'key' di posisi kosong yang sudah pas
        list_harga[j + 1] = key
    return list_harga

# ==============================================================================
# MAIN PROGRAM
# ==============================================================================
def main():
    file_db = "buku.txt"
    # Pastikan file buku.txt sudah ada dengan format: kode,judul,harga
    data_buku = muat_data_buku(file_db)
    list_promosi = LinkedListPromosi()
    antrean_toko = AntreanKasir()
    riwayat_transaksi = [150000, 50000, 200000, 75000, 120000]

    while True:
        print("\n--- SISTEM MANAJEMEN TOKO BUKU ---")
        print("1. Lihat Katalog Buku (Dictionary)")
        print("2. Kelola Daftar Promosi (Linked List)")
        print("3. Kelola Antrean Kasir (Queue)")
        print("4. Lihat Laporan Penjualan Terurut (Sorting)")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            print("\nData Katalog:")
            for k, v in data_buku.items():
                print(f"ID: {k} | {v['judul']} | Rp{v['harga']}")
        
        elif pilihan == '2':
            judul_baru = input("Masukkan judul buku untuk promosi: ")
            list_promosi.tambah_buku_promosi(judul_baru)
            list_promosi.tampilkan_promosi()

        elif pilihan == '3':
            print("\n--- Menu Antrean Kasir ---")
            print("1. Tambah Antrean (Nama)")
            print("2. Layani Pelanggan")
            sub_pilihan = input("Pilih tindakan (1/2): ")

            if sub_pilihan == '1':
                nama = input("Masukkan nama pelanggan: ")
                antrean_toko.tambah_antrean(nama)
            elif sub_pilihan == '2':
                antrean_toko.layani_pelanggan()
            else:
                print("Pilihan tidak tersedia.")

        elif pilihan == '4':
            print("Harga Sebelum Urut:", riwayat_transaksi)
            # Mengirimkan copy list agar data asli tidak berubah jika diperlukan
            hasil_sort = urutkan_transaksi(riwayat_transaksi[:])
            print("Harga Sesudah Urut:", hasil_sort)

        elif pilihan == '5':
            print("Keluar sistem...")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()