<<<<<<< HEAD
#================================================
# Nama : Farras Rahman Hakim
# NIM : J0403251088
# Kelas : TPL B1
#================================================

#================================================
# Latihan 2 : Melengkapi Kode
#================================================

#Soal 1 : Menjadi sorting Ascending
def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        
        data[j + 1] = key
    
    return data

#Soal 2 : Menjadi Descending
def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        
        while j >= 0 and data[j] < key:
            data[j + 1] = data[j]
            j -= 1
        
        data[j + 1] = key
    
=======
#================================================
# Nama : Farras Rahman Hakim
# NIM : J0403251088
# Kelas : TPL B1
#================================================

#================================================
# Latihan 2 : Melengkapi Kode
#================================================

#Soal 1 : Menjadi sorting Ascending
def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        
        data[j + 1] = key
    
    return data

#Soal 2 : Menjadi Descending
def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        
        while j >= 0 and data[j] < key:
            data[j + 1] = data[j]
            j -= 1
        
        data[j + 1] = key
    
>>>>>>> e8fe87d9f99109e9fc3362abdb3458300d0f17b3
    return data