def P2(x, y):
    num = x ^ y
    a = bin(num)
    x = a.count('1')
    return x

P2(1, 4)
P2(3, 1)
P2(123456, 54321)
