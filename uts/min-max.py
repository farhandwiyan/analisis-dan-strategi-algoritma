def MinMax(arr, i, j):
    length = j - i + 1
    
    if length == 1:
        return arr[i], arr[j]
    elif length <= 2:
        if arr[i] > arr[j]:
            min = arr[j]
            max = arr[i]
        else:
            min = arr[i]
            max = arr[j]
        
        return min, max
    else:
        tengah = (i + j) // 2
        
        min1, max1 = MinMax(arr, i, tengah)
        min2, max2 = MinMax(arr, tengah + 1, j)
        
        if min1 > min2:
            finalMin = min2
        else:
            finalMin = min1
        
        if max2 > max1:
            finalMax = max2
        else:
            finalMax = max1
        
        return finalMin, finalMax
        
        
arr = [8, 9, 10, 8, 1]
print(MinMax(arr, 0, len(arr) - 1))    