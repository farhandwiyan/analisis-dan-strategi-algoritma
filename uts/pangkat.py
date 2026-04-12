def pangkat(a, n):
    if n == 0:
        return 1
    else:
        x = pangkat(a, n // 2)
        if n % 2 == 0:
            return x * x
        else:
            return a * x * x
        
print(pangkat(2, 3))