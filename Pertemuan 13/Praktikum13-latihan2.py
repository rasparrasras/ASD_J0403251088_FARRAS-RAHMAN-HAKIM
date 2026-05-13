#=========================================
# Nama  : Farras Rahman Hakim
# NIM   : J0403251088
# Kelas : TPL B1
#=========================================
# Latihan 2 : Implementasi Algoritma Kruskal
#=========================================

# Daftar edge: (bobot, node1, node2) 
edges = [ 
    (1, 'C', 'D'), 
    (2, 'A', 'C'), 
    (3, 'B', 'D'), 
    (4, 'A', 'B'), 
    (5, 'A', 'D') 
] 

# 1. Mengurutkan edge berdasarkan bobot terkecil 
edges.sort() 

mst = [] 
total_weight = 0 
connected = set() # Set untuk melacak node yang sudah terhubung

# 2. Iterasi melalui edge yang sudah diurutkan
for weight, u, v in edges: 
    # Memilih edge jika salah satu node belum ada dalam set connected 
    # (Logika sederhana untuk mencegah cycle pada graph ini)
    if u not in connected or v not in connected: 
        mst.append((u, v, weight)) 
        total_weight += weight 
        
        # Tambahkan node ke dalam set
        connected.add(u) 
        connected.add(v) 

# Menampilkan hasil
print("Minimum Spanning Tree:") 
for edge in mst: 
    print(edge) 

print("Total bobot =", total_weight)

# Pertanyaan Analisis: 
# 1. Edge mana yang dipilih pertama kali? 
# 2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu? 
# 3. Berapa total bobot MST yang dihasilkan? 
# 4. Mengapa edge tertentu tidak dipilih?

# Jawaban Analisis:
# 1. Edge yang dipilih pertama kali adalah (1, 'C', 'D') karena memiliki bobot terkecil.
# 2. Edge dengan bobot paling kecil dipilih lebih dahulu untuk memastikan bahwa total bobot MST yang dihasilkan adalah minimum.
# 3. Total bobot MST yang dihasilkan adalah 6, dengan edge (1, 'C', 'D'), (2, 'A', 'C'), dan (3, 'B', 'D').
# 4. Edge tertentu tidak dipilih karena akan membentuk cycle atau karena sudah ada kedua node yang terhubung dalam set connected, sehingga tidak diperlukan untuk menghubungkan semua node.