#=========================================
# Nama : Farras Rahman Hakim
# NIM : J0403251088
# Kelas : TPL B1
#=========================================
# latihan 1
#=========================================

graph = { 
'A': ['B', 'C'], 
'B': ['D', 'E'], 
'C': ['F'], 
'D': [], 
'E': [], 
'F': [] 
}

def dfs(graph, node, visited): 
    visited.add(node) 
    print(node, end=" ") 
    
    for neighbor in graph[node]: 
        if neighbor not in visited: 
            dfs(graph, neighbor, visited) 

visited = set() 

print("DFS dari A:") 
dfs(graph, 'A', visited)

# Pertanyaan Analisis 
# 1. Mengapa DFS masuk ke node terdalam terlebih dahulu?  
# 2. Apa yang terjadi jika urutan neighbor diubah?  
# 3. Bandingkan hasil DFS dengan BFS pada graph yang sama. 
# Jawaban
# 1. DFS masuk ke node terdalam terlebih dahulu karena algoritma ini menggunakan pendekatan rekursif atau tumpukan (stack) untuk menyimpan node yang akan dikunjungi berikutnya. Ketika DFS mengunjungi sebuah node, ia langsung melanjutkan ke salah satu tetangganya tanpa menyelesaikan semua tetangga pada tingkat yang sama terlebih dahulu, sehingga menjelajahi jalur hingga mencapai node terdalam sebelum kembali dan menjelajahi jalur lainnya.
# 2. Jika urutan neighbor diubah, maka urutan kunjungan node dalam DFS juga akan berubah. Misalnya, jika dalam graph awal tetangga 'A' adalah ['B', 'C'], dan diubah menjadi ['C', 'B'], maka DFS akan mengunjungi 'C' terlebih dahulu sebelum 'B', sehingga menghasilkan urutan kunjungan yang berbeda.
# 3. Hasil DFS dan BFS pada graph yang sama akan berbeda karena kedua algoritma memiliki pendekatan yang berbeda dalam menjelajahi graph. DFS akan menjelajahi jalur terdalam terlebih dahulu, sedangkan BFS akan menjelajahi semua tetangga pada tingkat yang sama sebelum melanjutkan ke tingkat berikutnya. Oleh karena itu, urutan kunjungan node dalam DFS dan BFS akan berbeda, meskipun mereka mengunjungi node yang sama pada akhirnya.