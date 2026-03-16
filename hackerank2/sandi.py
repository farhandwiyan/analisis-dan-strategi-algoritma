def sandi_geometri(N, P):
    max = -1
    
    # jika N < 4, maka 4 titik tidak akan ditemukan
    if N >= 4:
        
        # mencari jumlah luas maksimal dengan mencari 2 titik terlebih dahulu, menghitung tinggi dan lebar,
        # lalu membandingkan luas saat ini dengan max
        # mencari 2 titik dengan kondisi x1 != x2 dan y1 != y2 yang kemungkinan diagonal dari persegi panjang
        # cari 2 titik lainnya yang dapat membentuk persegi panjang
        for i in range(N):
            x1, y1 = P[i]
            for j in range(i+1, N):
                x2, y2 = P[j]
                
                if x1 != x2 or y1 != y2:
                    found1 =  False
                    found2 = False
                    
                    for k in range(N):
                        if P[k][0] == x1 and P[k][1] == y2:
                            found1 = True
                        if P[k][0] == x2 and P[k][1] == y1:
                            found2 = True

                    if found1 and found2:
                        luas = abs(x2 - x1) * abs(y2 - y1)
                    
                        if max < luas:
                            max = luas
                        
        return max
    return max