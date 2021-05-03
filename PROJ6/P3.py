def P3(num):
    a = bin(num)[2:]
    b = a[::-1]
    n = 32 - len(b)
    c = b + '0' * n
    c = int(c, 2)
    return c