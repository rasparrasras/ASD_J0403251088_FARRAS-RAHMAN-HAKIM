# ==========================================================
# Tugas Hands-on: Manajemen Stok Barang Kantin
# Mata Kuliah: Algoritma dan Struktur Data (TPL2106)
# ==========================================================

NAMA_FILE = 'stok_barang.txt'

# --- Fungsi 1: Membaca Data dari File ---
def baca_stok(nama_file):
    """
    Membaca data dari file teks ke dalam dictionary di memori.
    Format file: KodeBarang,NamaBarang,Stok
    """
    stok_dict = {}
    try:
        with open(nama_file, 'r', encoding='utf-8') as file:
            for baris in file:
                baris = baris.strip()
                if baris: # Pastikan baris tidak kosong
                    kode, nama, stok = baris.split(',')
                    # Simpan ke dictionary: key adalah kode, value adalah dict nama & stok
                    stok_dict[kode] = {
                        'nama': nama,
                        'stok': int(stok)
                    }
    except FileNotFoundError:
        # Jika file belum ada, buat file kosong baru
        open(nama_file, 'w').close()
    return stok_dict

# --- Fungsi 2: Menu 1 - Tampilkan Semua Barang ---
def tampilkan_semua(stok_dict):
    if not stok_dict:
        print("\n[Peringatan] Stok barang kosong.")
        return

    print("\n" + "="*40)
    print(f"{'KODE':<10} | {'NAMA BARANG':<15} | {'STOK':<5}")
    print("-" * 40)
    for kode in sorted(stok_dict.keys()):
        nama = stok_dict[kode]['nama']
        stok = stok_dict[kode]['stok']
        print(f"{kode:<10} | {nama:<15} | {stok:<5}")
    print("="*40)

# --- Fungsi 3: Menu 2 - Cari Barang Berdasarkan Kode ---
def cari_barang(stok_dict):
    kode_cari = input("Masukkan kode barang yang dicari: ").strip()
    if kode_cari in stok_dict:
        data = stok_dict[kode_cari]
        print(f"\n[Data Ditemukan]")
        print(f"Kode: {kode_cari} | Nama: {data['nama']} | Stok: {data['stok']}")
    else:
        print("\nBarang tidak ditemukan.")

# --- Fungsi 4: Menu 3 - Tambah Barang Baru ---
def tambah_barang(stok_dict):
    kode = input("Masukkan kode barang baru: ").strip()
    if kode in stok_dict:
        print("Kode sudah digunakan.")
        return
    
    nama = input("Masukkan nama barang: ").strip()
    try:
        stok = int(input("Masukkan stok awal: "))
        if stok < 0:
            print("Stok tidak boleh negatif!")
            return
        
        # Tambahkan ke dictionary
        stok_dict[kode] = {'nama': nama, 'stok': stok}
        print(f"Barang {nama} berhasil ditambahkan.")
    except ValueError:
        print("Input stok harus berupa angka.")

# --- Fungsi 5: Menu 4 - Update Stok Barang ---
def update_stok(stok_dict):
    kode = input("Masukkan kode barang yang akan diupdate: ").strip()
    if kode not in stok_dict:
        print("Barang tidak ditemukan.")
        return
    
    print("1. Tambah stok")
    print("2. Kurangi stok")
    pilihan = input("Pilih aksi (1/2): ")
    
    try:
        jumlah = int(input("Masukkan jumlah: "))
        if jumlah < 0:
            print("Jumlah tidak boleh negatif.")
            return

        if pilihan == "1":
            stok_dict[kode]['stok'] += jumlah
            print("Stok berhasil ditambah.")
        elif pilihan == "2":
            if stok_dict[kode]['stok'] - jumlah < 0:
                print("Error: Stok tidak boleh negatif setelah dikurangi!")
            else:
                stok_dict[kode]['stok'] -= jumlah
                print("Stok berhasil dikurangi.")
        else:
            print("Pilihan menu tidak valid.")
    except ValueError:
        print("Input harus berupa angka.")

# --- Fungsi 6: Menu 5 - Simpan ke File ---
def simpan_ke_file(nama_file, stok_dict):
    with open(nama_file, 'w', encoding='utf-8') as file:
        for kode in sorted(stok_dict.keys()):
            nama = stok_dict[kode]['nama']
            stok = stok_dict[kode]['stok']
            file.write(f"{kode},{nama},{stok}\n")
    print(f"\nData berhasil disimpan ke {nama_file}.")

# --- Program Utama ---
def main():
    # Inisialisasi data dari file
    stok_barang = baca_stok(NAMA_FILE)
    
    while True:
        print("\n=== MENU STOK KANTIN ===")
        print("1. Tampilkan Semua Barang")
        print("2. Cari Barang Berdasarkan Kode")
        print("3. Tambah Barang Baru")
        print("4. Update Stok Barang")
        print("5. Simpan ke File")
        print("0. Keluar")
        
        pilihan = input("Masukkan pilihan menu: ").strip()
        
        if pilihan == "1":
            tampilkan_semua(stok_barang)
        elif pilihan == "2":
            cari_barang(stok_barang)
        elif pilihan == "3":
            tambah_barang(stok_barang)
        elif pilihan == "4":
            update_stok(stok_barang)
        elif pilihan == "5":
            simpan_ke_file(NAMA_FILE, stok_barang)
        elif pilihan == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()