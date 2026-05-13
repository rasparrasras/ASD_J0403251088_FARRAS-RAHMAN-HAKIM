<<<<<<< HEAD
#=========================================
# Nama : Farras Rahman Hakim
# NIM : J0403251088
# Kelas : TPL B1
#=========================================
# Latihan 1 :  Weighted Graph dan Perhitungan Jalur
#=========================================

# Representasi weighted graph menggunakan dictionary bersarang 
graph = { 
'A': {'B': 4, 'C': 2}, 
'B': {'D': 5}, 
'C': {'D': 1}, 
'D': {} 
} 
# Menghitung dua kemungkinan jalur dari A ke D 
jalur_1 = graph['A']['B'] + graph['B']['D'] # A -> B -> D 
jalur_2 = graph['A']['C'] + graph['C']['D'] # A -> C -> D

print("Jalur 1: A -> B -> D =", jalur_1) 
print("Jalur 2: A -> C -> D =", jalur_2) 

if jalur_1 < jalur_2: 
    print("Jalur terpendek adalah A -> B -> D") 
else: 
    print("Jalur terpendek adalah A -> C -> D")

# Pertanyaan Analisis: 
# 1. Berapa total bobot jalur A -> B -> D? 
# 2. Berapa total bobot jalur A -> C -> D? 
# 3. Jalur mana yang dipilih sebagai jalur terpendek? 
# 4. Mengapa jalur terpendek tidak selalu ditentukan dari jumlah edge yang paling sedikit?

#Jawaban Analisis:
# 1. Total bobot jalur A -> B -> D adalah 4 + 5 = 9.
# 2. Total bobot jalur A -> C -> D adalah 2 + 1 = 3.
# 3. Jalur yang dipilih sebagai jalur terpendek adalah A -> C   -> D karena memiliki total bobot yang lebih kecil (3) dibandingkan dengan jalur A -> B -> D (9).
=======
#=========================================
# Nama : Farras Rahman Hakim
# NIM : J0403251088
# Kelas : TPL B1
#=========================================
# Latihan 1 :  Weighted Graph dan Perhitungan Jalur
#=========================================

# Representasi weighted graph menggunakan dictionary bersarang 
graph = { 
'A': {'B': 4, 'C': 2}, 
'B': {'D': 5}, 
'C': {'D': 1}, 
'D': {} 
} 
# Menghitung dua kemungkinan jalur dari A ke D 
jalur_1 = graph['A']['B'] + graph['B']['D'] # A -> B -> D 
jalur_2 = graph['A']['C'] + graph['C']['D'] # A -> C -> D

print("Jalur 1: A -> B -> D =", jalur_1) 
print("Jalur 2: A -> C -> D =", jalur_2) 

if jalur_1 < jalur_2: 
    print("Jalur terpendek adalah A -> B -> D") 
else: 
    print("Jalur terpendek adalah A -> C -> D")

# Pertanyaan Analisis: 
# 1. Berapa total bobot jalur A -> B -> D? 
# 2. Berapa total bobot jalur A -> C -> D? 
# 3. Jalur mana yang dipilih sebagai jalur terpendek? 
# 4. Mengapa jalur terpendek tidak selalu ditentukan dari jumlah edge yang paling sedikit?

#Jawaban Analisis:
# 1. Total bobot jalur A -> B -> D adalah 4 + 5 = 9.
# 2. Total bobot jalur A -> C -> D adalah 2 + 1 = 3.
# 3. Jalur yang dipilih sebagai jalur terpendek adalah A -> C   -> D karena memiliki total bobot yang lebih kecil (3) dibandingkan dengan jalur A -> B -> D (9).
>>>>>>> e8fe87d9f99109e9fc3362abdb3458300d0f17b3
# 4. Jalur terpendek tidak selalu ditentukan dari jumlah edge yang paling sedikit karena dalam weighted graph, setiap edge memiliki bobot atau biaya yang berbeda. Sebuah jalur dengan jumlah edge yang lebih sedikit bisa memiliki bobot yang lebih besar dibandingkan dengan jalur yang memiliki lebih banyak edge tetapi dengan bobot yang lebih kecil. Oleh karena itu, untuk menentukan jalur terpendek dalam weighted graph, kita harus mempertimbangkan total bobot dari jalur tersebut, bukan hanya jumlah edge.