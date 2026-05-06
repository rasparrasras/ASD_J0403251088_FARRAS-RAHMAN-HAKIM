#=========================================
# Nama : Farras Rahman Hakim
# NIM  : J0403251088
# Kelas: TPL B1
#=========================================
# Latihan 5: Studi Kasus Jalur Terpendek Antar Kota
# Algoritma: Dijkstra 
# ==========================================================

import heapq

# 1. Representasi graph berbobot menggunakan dictionary
# Bobot menunjukkan jarak atau waktu antar kota
graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},
    'Depok': {'Jakarta': 2, 'Bandung': 6},
    'Jakarta': {'Bandung': 7},
    'Bandung': {}
}

# 2. Fungsi Dijkstra
def dijkstra(graph, start):
    # Inisialisasi jarak semua node dengan tak terhingga
    distances = {node: float('inf') for node in graph}
    distances[start] = 0 

    # Priority queue untuk menyimpan (jarak, node)
    priority_queue = [(0, start)] 

    while priority_queue:
        # Ambil node dengan jarak terkecil dari queue
        current_distance, current_node = heapq.heappop(priority_queue)

        # Jika ditemukan jarak yang lebih jauh dari yang sudah dicatat, abaikan
        if current_distance > distances[current_node]: 
            continue 

        # Periksa tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight 
            
            # Jika ditemukan jalur yang lebih pendek, perbarui data
            if distance < distances[neighbor]: 
                distances[neighbor] = distance 
                heapq.heappush(priority_queue, (distance, neighbor)) 
    return distances 

# 3. Penentuan node awal (Bogor)
start_node = 'Bogor'
hasil = dijkstra(graph, start_node) 

# 4. Output jarak terpendek dari node awal ke semua node
print(f"Jarak terpendek dari {start_node}:") 
for kota, jarak in hasil.items(): 
    print(f"{start_node} -> {kota} = {jarak}")

# Pertanyaan Analisis: 
# 1. Node awal yang digunakan apa? 
# 2. Node mana yang memiliki jarak paling kecil dari node awal? 
# 3. Node mana yang memiliki jarak paling besar dari node awal? 
# 4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus yang Anda buat.

# Jawaban Analisis:
# 1. Node awal yang digunakan adalah Bogor.
# 2. Node yang memiliki jarak paling kecil dari Bogor (selain Bogor itu sendiri) adalah Depok dengan jarak 2.
# 3. Node yang memiliki jarak paling besar dari Bogor adalah Bandung dengan jarak 8.
# 4. Cara kerja Dijkstra pada kasus ini:
#    - Algoritma mulai dari Bogor (jarak 0). 
#    - Ia memeriksa tetangga Bogor: Depok (2) dan Jakarta (5).
#    - Dari Depok, ia melihat jalur ke Jakarta. Totalnya menjadi 2 + 2 = 4. 
#      Karena 4 lebih kecil dari 5 (jalur langsung Bogor-Jakarta), maka jarak Jakarta diperbarui ke 4.
#    - Dari Depok ke Bandung adalah 2 + 6 = 8.
#    - Dari Jakarta ke Bandung adalah 4 + 7 = 11.
#    - Hasil akhir mengambil yang terkecil, sehingga Bandung tercatat dengan jarak 8.