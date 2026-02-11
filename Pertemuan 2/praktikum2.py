#======================================
# Praktikum 2: Konsep ADT dan File Handling
# Latihan 1: Membuat fungsi load data
#======================================

from multiprocessing.util import info


nama_file = 'Data_mahasiswa.txt'
data_dict = {} # Inisialisasi dictionary kosong untuk menyimpan data

def baca_data_mahsiswa(nama_file):
    with open(nama_file, 'r', encoding='utf-8') as file:
        for baris in file:
            # Menghapus karakter newline dan memisahkan data berdasarkan koma
            nim, nama, nilai= baris.split(',')
            # Menyimpan data ke dalam dictionary dengan NIM sebagai kunci
            data_dict[nim] = {
                'nama': nama,
                'nilai': int(nilai),
            }
    return data_dict
# Memanggil fungsi dan menampilkan hasilnya
buka_data = baca_data_mahsiswa(nama_file)
#print('jumlah data terbaca =', len(buka_data))

#======================================
# Praktikum 2: Konsep ADT dan File Handling
# Latihan 2: Membuat fungsi menampilkan data
#======================================

def tampil_data_mahasiswa(data_dict):

    if len(data_dict) == 0:
        print("Data mahasiswa kosong.")
        return

    # Menampilkan header tabel
    print("\nData Mahasiswa:")
    print(f"{'NIM':10} {'Nama':<12} {'Nilai':10}")
    print("-" * 40)
    for nim in sorted(data_dict.keys()):
        nama = data_dict[nim]['nama']
        nilai = data_dict[nim]['nilai']
        print(f"{nim:<10} {nama:<12} {nilai:<10}")

# Memanggil fungsi untuk menampilkan data
#tampil_data_mahasiswa(buka_data)

#======================================
# Praktikum 2: Konsep ADT dan File Handling
# Latihan 3: Membuat fungsi mencari data
#====================================== 

def cari_data_mahasiswa(data_dict, nim_cari):
    if nim_cari in data_dict:
        nama = data_dict[nim_cari]['nama']
        nilai = data_dict[nim_cari]['nilai']
        print(f"\nData ditemukan:")
        print(f"NIM: {nim_cari}")
        print(f"Nama: {nama}")
        print(f"Nilai: {nilai}")
    else:
        print(f"\nData dengan NIM {nim_cari} tidak ditemukan.")

# Meminta input NIM dari pengguna
#nim_input = input("\nMasukkan NIM yang ingin dicari: ")
#cari_data_mahasiswa(buka_data, nim_input)

#======================================
# Praktikum 2: Konsep ADT dan File Handling
# Latihan 4: Membuat fungsi update nilai
#======================================

def update_nilai_mahasiswa(data_dict):

    #cari nim yang akan diupdate nilainya
    nim = input("\nMasukkan NIM mahasiswa yang nilainya ingin diupdate: ").strip()
    if nim not in data_dict:
        print(f"\nData tidak ditemukan. Update nilai dibatalkan.")
        return
    try:
        nilai_baru = int(input("Masukkan nilai baru: "))
    except ValueError:
        print("Nilai harus berupa angka. Update nilai dibatalkan.")
        return
    
    if nilai_baru < 0 or nilai_baru > 100:
        print("Nilai harus berada antara 0 dan 100. Update nilai dibatalkan.")
        return

    nilai_lama = data_dict[nim]['nilai']
    data_dict[nim]['nilai'] = nilai_baru
    
    print(f'Update nilai berhasil!. Nilai {nim} dari {nilai_lama} menjadi {nilai_baru}')

#update_nilai_mahasiswa(buka_data)

#======================================
# Praktikum 2: Konsep ADT dan File Handling
# Latihan 5: Membuat fungsi menyimpan data ke file
#======================================

def simpan_data_mahasiswa(nama_file, data_dict):
    with open(nama_file, 'w', encoding='utf-8') as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]['nama']
            nilai = data_dict[nim]['nilai']
            baris = f"{nim},{nama},{nilai}\n"
            file.write(baris)
    print(f"\nData berhasil disimpan ke file {nama_file}.")
# Memanggil fungsi untuk menyimpan data
#simpan_data_mahasiswa(nama_file, buka_data)

#======================================
# Praktikum 2: Konsep ADT dan File Handling
# Latihan 6: Membuat menu program
#======================================

def main():

    #menjalankan fungsi 1 load data
    buka_data = baca_data_mahsiswa(nama_file)

while True:
    print("\n============Menu Data Mahsiswa:=============")
    print("1. Tampilkan Data Mahasiswa")
    print("2. Cari Data Mahasiswa")
    print("3. Update Nilai Mahasiswa")
    print("4. Simpan Data ke File")
    print("0. Keluar")

    pilihan = input("Masukkan pilihan menu: ")

    if pilihan == "1":
        tampil_data_mahasiswa(buka_data)
    elif pilihan == "2":
        nim_input = input("Masukkan NIM yang ingin dicari: ")
        cari_data_mahasiswa(buka_data, nim_input)
    elif pilihan == "3":
        update_nilai_mahasiswa(buka_data)
    elif pilihan == "4":
        simpan_data_mahasiswa(nama_file, buka_data)
    elif pilihan == "0":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

# Menjalankan program utama
if __name__ == "__main__":
    main()