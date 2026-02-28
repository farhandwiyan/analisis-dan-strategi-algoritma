N = 8
Q = 3
A = [1,2,2,2,3,2,2,1]
q = [(1,8), (2,5), (5,8)]

for i in range(Q):
    awal = q[i][0]              # index awal yang dicari
    akhir = q[i][1]             # index akhir yang dicari
    total = akhir - awal + 1    # total dari jumlah elemen yang ada di antara awal - akhir
    frek = {}                   # list yang berisi jumlah kemunculan angka
    
    # mencari frekuensi dari masing masing angka yang ada di index awal - akhir
    # memasukan frekuensi dari setiap elemen ke dalam list frek,
    # setiap index dari list frek menggambarkan jumlah kemunculan angka di dalam rentang awal - akhir
    # contoh: frek[2] = 3 -> jumlah kemunculan angka 2 di list A = 3
    for j in range(awal-1, akhir):
        nilai = A[j]
        if nilai in frek:
            frek[nilai] += 1
        else:
            frek[nilai] = 1
    
    # mencari elemen dari list frek yang > total / 2
    for k in frek:
        if frek[k] > (total // 2):
            print(k)
            break
    else:
        print(-1)


# ===============================
# ===== dalam bentuk funngsi ====
# ===============================

# def distrikDominan(N, Q, A, q):
#     hasil = [0] * Q
    
#     for i in range(Q):
#         awal = q[i][0]
#         akhir = q[i][1]
#         total = akhir - awal + 1
#         frek = [0] * N
        
#         for j in range(awal-1, akhir):
#             nilai = A[j]
#             frek[nilai] = frek[nilai] + 1
        
#         for k in range(N):
#             if frek[k] > (total // 2):
#                 hasil[i] = k
#                 break
#             else:
#                 hasil[i] = -1
                
#     return hasil

# print("Test 1 :", distrikDominan(8, 3, [1,2,2,2,3,2,2,1], [(1,8), (2,5), (5,8)]))