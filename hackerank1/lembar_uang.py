def lembarMinimun(X):
    uang = X    # total uang yag dicari
    lembar = 0  # jumlah lembar uang yg diperoleh
    
    # mencari jumlah lembar yang diperlukan berdasarkan nomimal uang
    while uang != 0:
        if uang >= 50:
            uang -= 50
            lembar += 1
        elif uang >= 25:
            uang -= 25
            lembar += 1
        elif uang >= 10:
            uang -= 10
            lembar += 1
        elif uang >= 5:
            uang -= 5
            lembar += 1
        else:
            uang -= 1
            lembar += 1
    
    return lembar

print(f"Test 1 : {lembarMinimun(37)}")
print(f"Test 2 : {lembarMinimun(3)}")