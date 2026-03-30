import random

def RandomizeDuplicate(arr, N):
    hasil = []
    count = N
    langkah = 0
    
    while count > 0:
        langkah += 1
        randIdx = random.randint(0, N-1)
        pivot = arr[randIdx]
        
        print(f"arr ke-{langkah} = {arr}")
        print(f"pivot ke-{langkah} = {pivot}")
        
        if pivot != -1:
            frek = 0
            
            for i in range(N):
                if arr[i] == pivot:
                    frek += 1
                    arr[i] = -1
            
            hasil.append(pivot)
            print(f"array hasil ke-{langkah} = {hasil}")
        
            count -= frek
        
        print()
    
    return hasil

nilai_list = [
 55, 65, 70, 75, 80,
 85, 90, 95, 100, 60,
 72, 68, 77, 83, 88,
 55, 65, 70, 75, 80,
 72, 68, 77, 83, 88,
 85, 90, 95, 100, 60,
 ]
print(RandomizeDuplicate(nilai_list, len(nilai_list)))
    
        
        