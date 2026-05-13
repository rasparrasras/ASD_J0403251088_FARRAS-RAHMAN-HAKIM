#=========================================
# Nama  : Farras Rahman Hakim
# NIM   : J0403251088
# Kelas : TPL B1
#=========================================
# Latihan 1 : Implementasi Spanning Tree
#=========================================

# 1. Daftar edge pada graph berdasarkan gambar
# Format: (node1, node2)
edges = [ 
    ('A', 'B'), 
    ('A', 'C'), 
    ('A', 'D'), 
    ('C', 'D'), 
    ('B', 'D') 
] 

# 2. Contoh Spanning Tree yang valid
# Spanning tree harus menghubungkan semua node (4 node) tanpa cycle.
# Jumlah edge pada spanning tree harus (n - 1), yaitu 3 edge.
spanning_tree = [ 
    ('A', 'C'), 
    ('C', 'D'), 
    ('B', 'D') 
] 

# Menampilkan daftar edge pada graph
print("Daftar edge pada graph:") 
for edge in edges: 
    print(edge) 

# Menampilkan contoh spanning tree yang valid
print("\nContoh Spanning Tree yang valid:") 
for edge in spanning_tree: 
    print(edge) 

# 3. Menampilkan jumlah edge pada graph awal
print("\nJumlah edge pada graph awal =", len(edges)) 

# 4. Menampilkan jumlah edge pada spanning tree
print("Jumlah edge pada spanning tree =", len(spanning_tree))

# Pertanyaan Analisis: 
# 1. Apa perbedaan graph awal dan spanning tree? 
# 2. Mengapa spanning tree tidak boleh memiliki cycle? 
# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit?

# Jawaban Analisis:
# 1. Graph awal memiliki semua edge yang menghubungkan node, sedangkan spanning tree hanya memiliki subset edge yang menghubungkan semua node tanpa cycle.
# 2. Spanning tree tidak boleh memiliki cycle karena cycle berarti ada lebih dari satu cara untuk menghubungkan node, yang tidak efisien dan tidak diperlukan untuk menghubungkan semua node.
# 3. Jumlah edge pada spanning tree selalu lebih sedikit karena spanning tree hanya membutuhkan (n - 1) edge untuk menghubungkan n node, sedangkan graph awal bisa memiliki lebih banyak edge yang menghubungkan node secara langsung atau tidak langsung.