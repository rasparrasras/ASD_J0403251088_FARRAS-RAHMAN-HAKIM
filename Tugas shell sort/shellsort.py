#================================================
# Nama : Farras Rahman Hakim
# NIM : J0403251088
# Kelas : TPL B1
#================================================

def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range (gap, n):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr [j - gap]
                j-= gap

            arr[j] = temp

        gap //= 2

    return arr

data =[9, 8, 3,7,5, 6, 4, 1]

print("Sebelum Sorting: ", data)
shell_sort(data)
print("Seteah Sorting: ", data)
