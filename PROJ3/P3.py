def P3(A, B):
    a = len(A)
    L1 = []
    for i in range(1, a+1):
        for j in range(a-i+1):
            if A[j:j+i].count(1) == B[j:j+i].count(1):
                L1.append(i)
            else:
                continue
    if len(L1) == 0:
        return 0
    m = max(L1)
    return m