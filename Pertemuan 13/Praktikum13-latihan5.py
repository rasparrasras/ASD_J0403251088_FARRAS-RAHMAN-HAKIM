#=========================================
# Nama  : Farras Rahman Hakim
# NIM   : J0403251088
# Kelas : TPL B1
#=========================================
# Latihan 5 : Studi Kasus Jaringan Antar Kota
#=========================================

# ========================================================== 
# Kasus 1: Jaringan Jalan Antar Kota (Algoritma Kruskal)
# ========================================================== 

# 1. Representasi Weighted Graph (Bobot, Kota1, Kota2)
# Data sesuai soal Kasus 1
daftar_jalan = [
    (5, 'Bogor', 'Jakarta'),
    (2, 'Bogor', 'Depok'),
    (3, 'Depok', 'Jakarta'),
    (6, 'Jakarta', 'Bandung'),
    (4, 'Depok', 'Bandung')
]

# 2. Implementasi Algoritma Kruskal
# Mengurutkan jalan berdasarkan jarak/bobot terpendek
daftar_jalan.sort()

mst_jalan = []
total_jarak = 0
kota_terhubung = set()

# Proses pemilihan jalur (Edge)
for bobot, k1, k2 in daftar_jalan:
    # Mengambil jalur jika salah satu kota belum terhubung 
    # untuk mencegah terbentuknya cycle/sirkuit
    if k1 not in kota_terhubung or k2 not in kota_terhubung:
        mst_jalan.append((k1, k2, bobot))
        total_jarak += bobot
        
        # Tambahkan kota ke set pemantau
        kota_terhubung.add(k1)
        kota_terhubung.add(k2)

# 3. Output Minimum Spanning Tree (MST)
print("Minimum Spanning Tree (Jalur Jalan Terpilih):")
for jalur in mst_jalan:
    print(f"{jalur[0]} - {jalur[1]} (Bobot: {jalur[2]})")

# 4. Output Total Bobot Minimum
print("-" * 40)
print("Total Bobot Minimum MST =", total_jarak)

# Pertanyaan Analisis: 
# 1. Kasus apa yang dipilih? 
# 2. Algoritma apa yang digunakan? 
# 3. Edge mana saja yang dipilih dalam MST? 
# 4. Berapa total bobot MST? 
# 5. Mengapa edge tertentu tidak dipilih?

#Jawaban Analisis:
# 1. Kasus yang dipilih adalah Jaringan Jalan Antar Kota (Kasus 1).
# 2. Algoritma yang digunakan adalah Kruskal's Algorithm, yang merupakan algoritma greedy untuk menemukan Minimum Spanning Tree (MST) dari sebuah graph berbobot.
# 3. Edge yang dipilih dalam MST adalah:
#    - Bogor - Depok (2)
#    - Depok - Jakarta (3)
#    - Depok - Bandung (4)
# 4. Total bobot MST adalah 9, dengan edge (2, 'Bogor', 'Depok'), (3, 'Depok', 'Jakarta'), dan (4, 'Depok', 'Bandung').
# 5. Edge tertentu tidak dipilih karena akan membentuk cycle atau karena sudah ada kedua kota yang terhubung dalam set kota_terhubung, sehingga tidak diperlukan untuk menghubungkan semua kota.