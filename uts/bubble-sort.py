def bubble(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] < arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
                print(f"arr ke-{i}: {arr}")
    return arr

print(bubble([2, 3, 1, 5, 6]))