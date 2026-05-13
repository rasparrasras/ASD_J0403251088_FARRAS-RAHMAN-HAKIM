#=========================================
# Nama : Farras Rahman Hakim
# NIM : J0403251088
# Kelas : TPL B1
#=========================================
# latihan 1
#=========================================

graph = { 
'Rumah': ['Sekolah', 'Toko'], 
'Sekolah': ['Perpustakaan'], 
'Toko': ['Pasar'], 
'Perpustakaan': [], 
'Pasar': []
}

from collections import deque 

def bfs(graph, start): 
    visited = set() 
    queue = deque([start]) 

    visited.add(start) 
    while queue: 
        node = queue.popleft() 
        print(node, end=" ") 

    for neighbor in graph[node]: 
        if neighbor not in visited: 
            visited.add(neighbor) 
            queue.append(neighbor) 
print("BFS dari Rumah:")
bfs(graph, 'Rumah')
#..................................... 
# Pertanyaan Analisis 
# 1. Node mana yang dikunjungi pertama?  
# 2. Mengapa BFS cocok untuk mencari jalur terdekat?  
# 3. Apa perbedaan urutan BFS jika struktur graph diubah?
#......................................
# Jawaban
# 1. Node yang pertama kali dikunjungi adalah Rumah. Hal ini karena 'Rumah' ditetapkan sebagai titik awal (start) pada pemanggilan fungsi, sehingga langsung dimasukkan ke dalam antrean (queue) dan ditandai telah dikunjungi pada tahap awal inisialisasi sebelum perulangan dimulai.
# 2. BFS cocok untuk mencari jalur terdekat karena algoritma ini menjelajahi semua tetangga pada tingkat yang sama sebelum melanjutkan ke tingkat berikutnya. Dengan cara ini, BFS memastikan bahwa jalur pertama yang ditemukan ke suatu node adalah jalur terpendek dalam hal jumlah edge (lompatan) dari titik awal ke node tersebut, sehingga sangat efektif untuk menemukan jalur terdekat dalam graph yang tidak berbobot.
# 3. Urutan BFS akan berubah jika struktur graph diubah karena BFS mengunjungi node berdasarkan urutan tetangga yang terdaftar dalam graph. Jika urutan tetangga diubah, maka urutan kunjungan node juga akan berubah. Misalnya, jika dalam graph awal tetangga 'Rumah' adalah ['Sekolah', 'Toko'], dan diubah menjadi ['Toko', 'Sekolah'], maka BFS akan mengunjungi 'Toko' terlebih dahulu sebelum 'Sekolah', sehingga menghasilkan urutan kunjungan yang berbeda.
