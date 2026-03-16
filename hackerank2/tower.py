def tower(R, C, P):
    total = -1
    
    # Mencari titik pusat yang berada dimulai dari baris kedua dan kolom kedua
    # Jika titik pusat genap lakukan penjulahan dengan titik diatas, dibawah, dikanan, dan dikiri dari titik pusat
    # jika total ganjil return nilai dari total, jika genap lanjut ke iterasi selanjutnya
    for i in range(1, R - 1):
        for j in range(1, C - 1):
            pusat = P[i][j]
            
            if pusat % 2 == 0:
                atas = P[i - 1][j]
                bawah = P[i + 1][j]
                kanan = P[i][j + 1]
                kiri = P[i][j - 1]
                
                total = pusat + atas + bawah + kanan + kiri
                
            if total % 2 == 1:
                return total
    
    return -1
                

print(tower(3, 3, [
    [1, 2, 1],
    [2, 4, 4],
    [1, 5, 1]
])
)

print(tower(4, 4, [
    [1, 1, 1],
    [1, 3, 1],
    [1, 1, 1]
])
      )    