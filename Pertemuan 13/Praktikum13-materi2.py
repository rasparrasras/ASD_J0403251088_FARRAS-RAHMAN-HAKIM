#=========================================
# Nama : Farras Rahman Hakim
# NIM : J0403251088
# Kelas : TPL B1
#=========================================
# Materi 1 : Implementasi Prim
#=========================================

import heapq 

# graph direpresentasikan sebagai adjacency list dengan bobot
graph = { 
    'A': {'B': 4, 'C': 2, 'D': 5}, 
    'B': {'A': 4, 'D': 3}, 
    'C': {'A': 2, 'D': 1}, 
    'D': {'A': 5, 'B': 3, 'C': 1} 
} 

# fungsi untuk mengimplementasikan Prim's algorithm
def prim(graph, start): 
 
    visited = set([start]) 
 
    edges = [] 
    # Tambahkan semua edge dari node awal ke heap
    for neighbor, weight in graph[start].items(): 
        heapq.heappush(edges, (weight, start, neighbor)) 
 
    mst = [] 
    total_weight = 0 
    # Proses heap hingga kosong
    while edges: 
 
        weight, u, v = heapq.heappop(edges) 

        if v not in visited: 
 
            visited.add(v) 
 
            mst.append((u, v, weight)) 
            total_weight += weight 
            # Tambahkan semua edge dari node baru ke heap
            for neighbor, w in graph[v].items(): 
 
                if neighbor not in visited: 
                    heapq.heappush(edges, (w, v, neighbor)) 
 
    return mst, total_weight 
 
# Jalankan Prim's algorithm mulai dari node 'A'
mst, total = prim(graph, 'A') 
 
print("Minimum Spanning Tree:") 
 
for edge in mst: 
    print(edge) 
 
print("Total bobot =", total)