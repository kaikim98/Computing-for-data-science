def P2(n, edges):
    L1 = []
    if len(edges) == 0:
        return 1
    for i in edges:
        if 1 in i:
            L1.append(list(i))
    L3 = []
    for i in L1:
        for j in i:
            L3.append(j)
    L4 = list(set(L3))
    L6 = []
    count = n
    while count == 0:
        curlist = L4
        L5 = []
        for i in curlist:
            for j in edges:
                if i in j:
                    L5.append(j)
        for i in L5:
            for j in i:
                L6.append(j)
        L6 = list(set(L6))
        if curlist == L6:
            break
        curlist = L6
        if 1 not in L6:
            L6.append(1)
        count = count -1
    L6 = list(set(L6))
    a = len(L6)
    return a

P2(7, [(1, 2), (2,3), (1,5), (5, 2), (5, 6), (4, 7)])
P2(1, [])
P2(3, [(1,2)])
P2(4, [(1, 2), (2, 1)])
P2(5, [(1,2), (2,3), (3,4), (4,5)])
