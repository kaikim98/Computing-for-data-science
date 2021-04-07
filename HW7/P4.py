def P4(A, B):
    list_1 = sorted(A)
    list_2 = sorted(B, reverse=True)
    n = len(list_1)
    s = 0
    for i in range(n):
        s = s+ list_1[i]*list_2[i]
    return s