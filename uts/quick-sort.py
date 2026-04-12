def partision(arr, low, high):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        
    arr[i+1], arr[high] = arr[high], arr[i+1]
    
    return i + 1

def quickSort(arr, low, high):
    if low < high:
        pi = partision(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
    
    return arr

arr = [1, 9, 8, 27, 10, 9, 28, 9, 3, 4]
print(quickSort(arr, 0, len(arr) - 1))
        