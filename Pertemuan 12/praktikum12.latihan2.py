#=========================================
# Nama : Farras Rahman Hakim
# NIM : J0403251088
# Kelas : TPL B1
#=========================================
# Latihan 2: Implementasi Dijkstra 
# ==========================================================

import heapq 
# Weighted graph dengan bobot positif 
graph = { 
    'A': {'B': 4, 'C': 2}, 
    'B': {'D': 5}, 
    'C': {'D': 1}, 
    'D': {} 
} 
def dijkstra(graph, start): 
    """ 
    Fungsi untuk mencari jarak terpendek dari node start 
    ke seluruh node lain menggunakan algoritma Dijkstra. 
    """ 
    # Semua jarak awal dibuat tak hingga 
    distances = {node: float('inf') for node in graph} 

    # Jarak dari start ke start adalah 0 
    distances[start] = 0 

    # Priority queue menyimpan pasangan (jarak, node) 
    priority_queue = [(0, start)]

    while priority_queue: 
        current_distance, current_node = heapq.heappop(priority_queue) 
 
        # Jika jarak saat ini lebih besar dari jarak yang sudah tercatat, 
        # maka proses dilewati 
        if current_distance > distances[current_node]: 
            continue 
 
        # Periksa semua tetangga dari node saat ini 
        for neighbor, weight in graph[current_node].items(): 
            distance = current_distance + weight 
 
            # Jika ditemukan jarak yang lebih kecil, perbarui jaraknya 
            if distance < distances[neighbor]: 
                distances[neighbor] = distance 
                heapq.heappush(priority_queue, (distance, neighbor)) 
 
    return distances 
 
 
hasil = dijkstra(graph, 'A') 
 
print("Jarak terpendek dari node A:") 
for node, distance in hasil.items(): 
    print(f"Jarak ke {node}: {distance}")

# Pertanyaan Analisis: 
# 1. Berapa jarak terpendek dari A ke B? 
# 2. Berapa jarak terpendek dari A ke C? 
# 3. Berapa jarak terpendek dari A ke D? 
# 4. Mengapa jarak A ke D lebih kecil melalui C dibandingkan melalui B? 
# 5. Apa fungsi priority_queue dalam algoritma Dijkstra? 
# 6. Mengapa Dijkstra tidak cocok untuk graph dengan bobot negatif?

# Jawaban analisis:
# 1. Jarak terpendek dari A ke B adalah 4.
# 2. Jarak terpendek dari A ke C adalah 2.
# 3. Jarak terpendek dari A ke D adalah 3.
# 4. Jarak A ke D lebih kecil melalui C dibandingkan melalui B karena bobot dari A ke C (2) ditambah bobot dari C ke D (1) menghasilkan total 3, sedangkan bobot dari A ke B (4) ditambah bobot dari B ke D (5) menghasilkan total 9. Oleh karena itu, jalur A -> C -> D lebih efisien dalam hal jarak dibandingkan dengan jalur A -> B -> D.
# 5. Fungsi priority_queue dalam algoritma Dijkstra adalah untuk menyimpan node-node yang akan diproses berdasarkan jarak terpendek yang telah ditemukan sejauh ini. Dengan menggunakan priority queue, algoritma dapat dengan cepat mengakses node dengan jarak terpendek berikutnya untuk diproses, sehingga meningkatkan efisiensi algoritma.
# 6. Dijkstra tidak cocok untuk graph dengan bobot negatif karena algoritma ini mengasumsikan bahwa setelah sebuah node diproses, jaraknya tidak akan berubah lagi. Jika terdapat bobot negatif, maka jarak ke node yang sudah diproses bisa menjadi lebih kecil jika melalui jalur lain yang memiliki bobot negatif, sehingga algoritma Dijkstra tidak dapat menjamin hasil yang benar dalam kasus tersebut.