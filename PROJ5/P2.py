def P2(n, edges):
    L1 = []
    L3 = []
    if len(edges) == 0:
        return 1
    for i in edges:
        if 1 in i:
           L1.append(i)
    L2 = []
    for i in L1:
         L2.append(list(i))
    L3 = []
    for i in L2:
        for j in i:
            L3.append(j)
    L4 = list(set(L3))
    L5 = []
    for i in L4:
        for j in edges:
            if i in j:
                L5.append(j)
    L6 = []
    for i in L5:
        for j in i:
            L6.append(j)
    L6 = list(set(L6))
    if 1 not in L6:
        L6.append(1)
    a = len(L6)
    return a
