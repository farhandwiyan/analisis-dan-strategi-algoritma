iterator = 0
firstPivot = None

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    
def partision(arr, low, high, isFirst, randIdx):
    if isFirst:
        swap(arr, randIdx, high)
        global firstPivot
        firstPivot = arr[high]

    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i = i + 1
            swap(arr, i, j)
            
    swap(arr, i + 1, high)
    return i + 1

def QuickSort(arr, low, high, isFirst, randIdx):
    global iterator
    iterator = iterator + 1
    if low < high:
        pi = partision(arr, low, high, isFirst, randIdx)
        QuickSort(arr, low, pi - 1, False, None)
        QuickSort(arr, pi + 1, high, False, None)
    
    return arr

print(QuickSort([9, 2, 7, 11, 1, 8, 5], 0, 6, True, 2))