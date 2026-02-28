def stabilitas(N, W): 
    if N < 2:   
        return -1
    
    total = 0           # total dari 3 bilangan terbesar
    g1 = g2 = g3 = 0    # 3 bilangan terbesar untuk ganjil
    genap = 0           # bilangan terbesar untuk genap
    
    # mmencari 3 bilangan ganjil terbesar dan 1 bilangan genap terbesar
    for i in range(N):
        if W[i] % 2 != 0:
            if W[i] > g1:
                g3 = g2
                g2 = g1
                g1 = W[i]
            elif W[i] > g2:
                g3 = g2
                g2 = W[i]
            elif W[i] > g3:
                g3 = W[i]
        else:
            if W[i] > genap:
                genap = W[i]
            
    # untuk mendapatkan nilai S ganjil: bilangan genap < 2
    if (g1 != 0 and g2 != 0) or g3 != 0:
        # bandingkan nilai ganjil terbesar ketiga dengan genap
        if g3 > genap:
            total = g1 + g2 + g3 
        else:
            total = g1 + g2 + genap
    else:
        total = -1
    
    return total
    
    
print(f"Test 1: {stabilitas(5, [2, 4, 6, 8, 10])}")
print(f"Test 2: {stabilitas(5, [1, 2, 3, 4, 5])}")
print(f"Test 3: {stabilitas(5, [10, 9, 8, 7, 6])}")
            
    
                
    
            
            
            