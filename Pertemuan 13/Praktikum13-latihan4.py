#=========================================
# Nama  : Farras Rahman Hakim
# NIM   : J0403251088
# Kelas : TPL B1
#=========================================
# Latihan 4 : Studi Kasus Jaringan Kabel
#=========================================

# 1. Representasi Weighted Graph menggunakan list of tuples
# Format: (biaya, gedung1, gedung2)
hubungan_gedung = [
    (4, 'GedungA', 'GedungB'),
    (2, 'GedungA', 'GedungC'),
    (3, 'GedungB', 'GedungD'),
    (1, 'GedungC', 'GedungD'),
    (5, 'GedungA', 'GedungD')
]

# 2. Implementasi Algoritma Kruskal
# Mengurutkan biaya pemasangan dari yang termurah ke termahal
hubungan_gedung.sort()

jaringan_optimum = []
total_biaya = 0
terhubung = set()

# Proses pemilihan jalur kabel (edge)
for biaya, g1, g2 in hubungan_gedung:
    # Memilih jalur jika salah satu gedung belum terhubung ke jaringan
    # (Mencegah pembentukan sirkuit/loop tertutup)
    if g1 not in terhubung or g2 not in terhubung:
        jaringan_optimum.append((g1, g2, biaya))
        total_biaya += biaya
        
        # Masukkan gedung ke dalam set gedung yang sudah memiliki akses internet
        terhubung.add(g1)
        terhubung.add(g2)

# 3. Output hasil jaringan kabel yang dipilih
print("Jalur Kabel yang Terpilih (MST):")
for jalur in jaringan_optimum:
    print(f"{jalur[0]} - {jalur[1]} dengan Biaya: {jalur[2]}")

# 4. Output total biaya minimum
print("-" * 30)
print("Total Biaya Minimum Pemasangan =", total_biaya)

# Pertanyaan Analisis: 
# 1. Algoritma apa yang digunakan? 
# 2. Edge mana saja yang dipilih? 
# 3. Berapa total biaya minimum? 
# 4. Mengapa MST cocok digunakan pada kasus ini?

# Jawaban Analisis:
# 1. Algoritma yang digunakan adalah Kruskal's Algorithm, yang merupakan algoritma greedy untuk menemukan Minimum Spanning Tree (MST) dari sebuah graph berbobot.
# 2. Edge yang dipilih adalah:
#    - (2, 'GedungA', 'GedungC')
#    - (1, 'GedungC', 'GedungD')
#    - (3, 'GedungB', 'GedungD')
# 3. Total biaya minimum adalah 6.
# 4. MST cocok digunakan pada kasus ini karena memastikan bahwa semua gedung terhubung dengan biaya minimum, tanpa membentuk sirkuit atau loop tertutup.   