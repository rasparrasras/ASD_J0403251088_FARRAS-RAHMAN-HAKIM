<<<<<<< HEAD
#================================================
# Nama : Farras Rahman Hakim
# NIM : J0403251088
# Kelas : TPL B1
#================================================

#================================================
# Merge Sort dengan Tracing
#================================================

def merge_sort(data, depth=0):
    indent = " " * depth #indentasi untuk visualisasi
    print(f"{indent}merge_sort: {data}")

    if len(data) <= 1:
        return data

    #Divide : membagi data menjadi 2 bagian
    mid = len(data) // 2
    left = data [:mid] #slicing bagian kiri
    right = data [mid:] #slicing bagian kanan

    print(f"{indent}Divide: Left => {left} | Right => {right}")

    #recursive call
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    merged = merge(left_sorted, right_sorted)
    print(f"{indent}Merge -> {merged}")

    return merge(left_sorted, right_sorted)

def merge(left_sorted, right_sorted):
    
    result = []
    i = j = 0

    #membandingkan elemen kiri dan kanan
    
    while i < len(left_sorted) and j < len(right_sorted):
        if left_sorted[i] <= right_sorted[j]:
            result.append(left_sorted[i])
            i += 1
        else:
            result.append(right_sorted[j])
            j += 1

    #menambahkan sisa elemen jika ada
    result.extend(left_sorted[i:])
    result.extend(right_sorted[j:])

    return result

#contoh penggunaan
angka = [13, 7, 28, 5, 19, 36, 4]
=======
#================================================
# Nama : Farras Rahman Hakim
# NIM : J0403251088
# Kelas : TPL B1
#================================================

#================================================
# Merge Sort dengan Tracing
#================================================

def merge_sort(data, depth=0):
    indent = " " * depth #indentasi untuk visualisasi
    print(f"{indent}merge_sort: {data}")

    if len(data) <= 1:
        return data

    #Divide : membagi data menjadi 2 bagian
    mid = len(data) // 2
    left = data [:mid] #slicing bagian kiri
    right = data [mid:] #slicing bagian kanan

    print(f"{indent}Divide: Left => {left} | Right => {right}")

    #recursive call
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    merged = merge(left_sorted, right_sorted)
    print(f"{indent}Merge -> {merged}")

    return merge(left_sorted, right_sorted)

def merge(left_sorted, right_sorted):
    
    result = []
    i = j = 0

    #membandingkan elemen kiri dan kanan
    
    while i < len(left_sorted) and j < len(right_sorted):
        if left_sorted[i] <= right_sorted[j]:
            result.append(left_sorted[i])
            i += 1
        else:
            result.append(right_sorted[j])
            j += 1

    #menambahkan sisa elemen jika ada
    result.extend(left_sorted[i:])
    result.extend(right_sorted[j:])

    return result

#contoh penggunaan
angka = [13, 7, 28, 5, 19, 36, 4]
>>>>>>> e8fe87d9f99109e9fc3362abdb3458300d0f17b3
print("Hasil Sorting: ", merge_sort(angka))