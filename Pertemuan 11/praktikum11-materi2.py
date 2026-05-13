#=========================================
# Nama : Farras Rahman Hakim
# NIM : J0403251088
# Kelas : TPL B1
#=========================================
# Implementasi BFS
#=========================================

#struktur data untuk membuat antrian, kita gunakan dari library collections
from collections import deque

#representasi graf
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

def bfs(graph, start):
    #fungsi untuk melakukan BFS
    # graph: representasi graf
    # start: node awal untuk BFS

    #queue diguankan untuk menyimpan node yang akan diproses
    queue = deque()  # buat antrian dan masukkan node awal

    #set untuk menyimpan node yang sudah dikunjungi
    visited = set()  

    #masukkan node awal ke queue
    queue.append(start)
    
    #tandai node awal sebagai node yang sudah dikunjungi
    visited.add(start)

    while queue:
        #mengambil node paling depan dari queue
        node = queue.popleft()
        #tamilkan node yang sedang diproses
        print(node, end=' ')

        #periksa semua tetangga dari node yang diambil
        for neighbor in graph[node]:
            #jika tetangga belum dikunjungi
            if neighbor not in visited:
                #tandai tetangga sebagai sudah dikunjungi
                visited.add(neighbor)

                #masukkan tetangga ke dalam queue untuk diproses nanti
                queue.append(neighbor)

#menjalankan BFS mulai dari node 'A'
bfs(graph, 'A')
