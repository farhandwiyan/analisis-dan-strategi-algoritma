def barisanSemut(x, y, n):
    hasil = []
    
    mul = 0     # kelipatan x
    length = 1  # panjang list hasil
    
    # menambahkan angka yang merupakan kelipatan x dan bukan kelipatan y
    # length akan bertambah jika panjang hasil list = n
    while length <= n:
        mul += x
        
        if mul % y != 0:
            hasil.append(mul)
            length += 1        
    
    return hasil


print(f"Test 1 : {barisanSemut(2, 3, 5)}")
print(f"Test 2 : {barisanSemut(1, 2, 10)}")
