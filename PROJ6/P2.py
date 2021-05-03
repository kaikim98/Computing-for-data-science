def P2(x, y):
    num = x ^ y
    a = bin(num)
    x = a.count('1')
    return x