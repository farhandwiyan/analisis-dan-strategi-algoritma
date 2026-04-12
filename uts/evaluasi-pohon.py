def isEmpty(tree):
    return tree == []

def info(tree):
    if isEmpty(tree):
        return None
    return tree[0]

def left(tree):
    if isEmpty(tree):
        return []
    return tree[1]

def right(tree):
    if isEmpty(tree):
        return []
    return tree[2]

def isDaun(tree):
    if isEmpty(tree):
        return False
    return left(tree) == [] and right(tree) == []

def evaluasiPohon(T):
    if isEmpty(left(T)) and isEmpty(right(T)):
        return info(T)
    else:
        kiri = evaluasiPohon(left(T))
        kanan = evaluasiPohon(right(T))
        
        if info(T) == "+":
            return kiri + kanan
        elif info(T) == "-":
            return kiri - kanan
        elif info(T) == "*":
            return kiri * kanan
        elif info(T) == "/":
            return kiri / kanan

T1 = ["*", [3, [], []], [5, [], []]]

print(evaluasiPohon(T1))