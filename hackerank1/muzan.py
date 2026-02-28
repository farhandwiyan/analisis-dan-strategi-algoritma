N = int(input())
A = list(map(int, input().split()))

C = []
for i in range(N):
    C.append(list(map(int, input().split())))

used = [False] * N

def muzan(last, total, count):
    if count == N:
        return total

    min = 99999999

    for i in range(N):
        if not used[i]:
            used[i] = True

            if last == -1:
                hasil = muzan(i, total + A[i], count + 1)
            else:
                hasil = muzan(i, total + A[i] + C[i][last], count + 1)

            if hasil < min:
                min = hasil

            used[i] = False

    return min


print(muzan(-1, 0, 0))