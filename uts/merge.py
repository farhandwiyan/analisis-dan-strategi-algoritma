def merge(arr, left, mid, right):
    # kamus
    B = [0] * (right + 1)
    
    # algoritma
    kiri1 = left
    kiri2 = mid + 1
    i = left
    
    while kiri1 <= mid and kiri2 <= right:
        if arr[kiri1] <= arr[kiri2]:
            B[i] = arr[kiri1]
            kiri1 += 1
        else:
            B[i] = arr[kiri2]
            kiri2 += 1
        i += 1
    
    while kiri1 <= mid:
        B[i] = arr[kiri1]
        kiri1 += 1
        i += 1
        
    while kiri2 <= right:
        B[i] = arr[kiri2]
        kiri2 += 1
        i += 1
    
    for i in range(left, right + 1):
        arr[i] = B[i]
            
def mergeSort(arr, i, j):
    if i < j:
        mid = (i + j) // 2
        mergeSort(arr, i, mid)
        mergeSort(arr, mid + 1, j)
        merge(arr, i, mid, j)

    return arr

def insertionSort(arr, i, j):
    if i < j:
        k = i
        insertionSort(arr, k+1, j)
        merge(arr, i, k, j)
    
    return arr

arr = [1, 9, 8, 27, 10, 9, 28, 9, 3, 4]
print(mergeSort(arr, 0, len(arr) - 1))
print(insertionSort(arr, 0, len(arr) - 1))