iterator = 0
firstPivot = None

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    
def partision(arr, low, high, isFirst, tesPivot):
    if isFirst:
        swap(arr, tesPivot, high)
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

def QuickSort(arr, low, high, isFirst, tesPivot):
    global iterator
    iterator = iterator + 1
    if low < high:
        pi = partision(arr, low, high, isFirst, tesPivot)
        QuickSort(arr, low, pi - 1, False, None)
        QuickSort(arr, pi + 1, high, False, None)
    
    return iterator

N = int(input())
arr =list(map(int, input().split()))

low = 0
high = N - 1

min_iterasi = 9999
index = 0
for i in range(N):
    arr_copy = []
    for i in range(N):
        arr_copy.append(arr[i])
    iterator = 0
    iterasi = QuickSort(arr, low, high, True, i)
    
    if iterasi < min_iterasi:
        min_iterasi = iterasi
        index = i 


print(f"Indeks Terbaik: {index} dengan {min_iterasi} iterasi")