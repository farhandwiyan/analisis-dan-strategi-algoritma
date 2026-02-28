# versi 1
def voucherBuku(n, T, N):
    max = -1    # nilai perkalian terbesar 
    
    # mencari 2 bilangan yang dijumlahkan sama dengan target
    for i in range(n):
        for j in range(0, n):
            if i != j:
                # mencari nilai perkalian paling tinggi dari 2 bilangan yang dijumlahkan sama dengan target
                if N[i] + N[j] == T and N[i] * N[j] > max:
                    max = N[i] * N[j]
    
    return max

# versi 2
def voucherBuku2(n, T, N):
    max = -1    # nilai perkalian terbesar 
    
    # mencari 2 bilangan yang dijumlahkan sama dengan target
    for i in range(n):
        for j in range(i+1, n):
            # mencari nilai perkalian paling tinggi dari 2 bilangan yang dijumlahkan sama dengan target
            if N[i] + N[j] == T and N[i] * N[j] > max:
                max = N[i] * N[j]
    
    return max


print(f"Test 1.1 :", voucherBuku(5, 10, [1, 9, 5, 5, 2]))
print(f"Test 1.2 :", voucherBuku(5, 10, [1, 9, 5, 5, 2]))

print(f"Test 2.1 :", voucherBuku2(4, 10, [2, 2, 5, 8]))
print(f"Test 2.2 :", voucherBuku2(4, 10, [2, 2, 5, 8]))
                
                    