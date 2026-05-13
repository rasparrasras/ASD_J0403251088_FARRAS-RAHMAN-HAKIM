#=========================================
# Nama  : Farras Rahman Hakim
# NIM   : J0403251088
# Kelas : TPL B1
#=========================================
# Latihan 3 : Implementasi Algoritma Prim
#=========================================

import heapq 

# Definisi graph menggunakan adjacency list (dictionary)
graph = { 
    'A': {'B': 4, 'C': 2, 'D': 5}, 
    'B': {'A': 4, 'D': 3}, 
    'C': {'A': 2, 'D': 1}, 
    'D': {'A': 5, 'B': 3, 'C': 1} 
} 

def prim(graph, start): 
    visited = set([start]) 
    edges = [] 
    
    # Masukkan semua edge dari node awal ke dalam priority queue (heap)
    for neighbor, weight in graph[start].items(): 
        heapq.heappush(edges, (weight, start, neighbor)) 
    
    mst = [] 
    total_weight = 0 
    
    while edges: 
        # Ambil edge dengan bobot terkecil
        weight, u, v = heapq.heappop(edges) 
        
        # Jika node tujuan belum dikunjungi, tambahkan ke MST
        if v not in visited: 
            visited.add(v) 
            mst.append((u, v, weight)) 
            total_weight += weight 
            
            # Tambahkan edge baru dari node yang baru saja dikunjungi
            for neighbor, w in graph[v].items(): 
                if neighbor not in visited: 
                    heapq.heappush(edges, (w, v, neighbor)) 
                    
    return mst, total_weight 

# Eksekusi algoritma Prim mulai dari node 'A'
mst, total = prim(graph, 'A') 

# Menampilkan hasil
print("Minimum Spanning Tree (Prim's Algorithm):") 
for edge in mst: 
    print(edge) 

print("Total bobot =", total)

# Pertanyaan Analisis:
# 1. Node awal apa yang digunakan? 
# 2. Edge mana yang dipilih pertama kali? 
# 3. Bagaimana Prim menentukan edge berikutnya? 
# 4. Berapa total bobot MST yang dihasilkan? 
# 5. Apa perbedaan pendekatan Prim dan Kruskal?

# Jawaban Analisis:
# 1. Node awal yang digunakan adalah 'A'.
# 2. Edge yang dipilih pertama kali adalah (2, 'A', 'C') karena memiliki bobot terkecil dari node 'A'.
# 3. Prim menentukan edge berikutnya dengan memilih edge dengan bobot terkecil yang menghubungkan node yang sudah dikunjungi dengan node yang belum dikunjungi.
# 4. Total bobot MST yang dihasilkan adalah 6, dengan edge (2, 'A', 'C'), (1, 'C', 'D'), dan (3, 'B', 'D').
# 5. Perbedaan pendekatan Prim dan Kruskal adalah Prim membangun MST dengan memulai dari satu node dan menambahkan edge dengan bobot terkecil yang menghubungkan node yang sudah dikunjungi dengan node yang belum dikunjungi, sedangkan Kruskal membangun MST dengan mengurutkan semua edge berdasarkan bobot dan menambahkan edge ke MST jika tidak membentuk cycle, tanpa memulai dari node tertentu.