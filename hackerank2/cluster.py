def hitungCluster(pusat, i, j, T):
    # hitung baris atas. bawah, dan baris pusat dari titik pusat
    baris_atas = T[i - 1][j - 1] + T[i - 1][j] + T[i - 1][j + 1]
    baris_bawah = T[i + 1][j - 1] + T[i + 1][j] + T[i + 1][j + 1]
    baris_pusat = T[i][j - 1] + pusat + T[i][j + 1]

    return baris_atas + baris_pusat + baris_bawah

def minMax(T, i, j):
    max = 0
    min = 999
    
    # cari nilai max dan min dari cluster berukuran 3 x 3
    for x in range(3):
        for y in range(3):
            val = T[i + x][j + y]
            
            if max < val:
                max = val
                
            if min > val:
                min = val
    
    return max, min


def cluster(R, C, D, T):
    max_suhu = -1
    
    for i in range(R - 2):
        for j in range(C - 2):
            
            # cari nilai min dan max dari masing-masing cluster
            max, min = minMax(T, i, j)
            
            if max - min >= D:
                # jika memeuhi syarat, hitung total suhu cluster dengan menggunakan 
                # patokan titik pusat dari cluster tersebut
                total_suhu = hitungCluster(T[i+1][j+1], i+1, j+1, T)
                

                if total_suhu > max_suhu:
                    max_suhu = total_suhu
    
    return max_suhu

print(cluster(4, 4, 10, [
    [5, 5, 5, 5],
    [5, 20, 5, 5],
    [5, 5, 5, 5],
    [2, 2, 2, 2]
]))

                
                
                
    
    
            
            
    
            
            
            
            