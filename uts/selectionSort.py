def partision(arr, low, high):
    idxMin = low
    
    for i in range(low+1, high+1):
        if arr[i] < arr[idxMin]:
            idxMin = i
    
    temp = arr[low]
    arr[low] = arr[idxMin] 
    arr[idxMin] = temp

def insertionSort(arr, low, high):
    if low < high:
        pi = partision(arr, low, high)
        insertionSort(arr, low+1, high)
    
    return arr

arr = [1, 9, 8, 27, 10, 9, 28, 9, 3, 4]
print(insertionSort(arr, 0, len(arr) - 1))