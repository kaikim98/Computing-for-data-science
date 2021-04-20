def P2(n, edges):
    # L1 = []
    # L3 = []
    # if len(edges) == 0:
    #     return 1
    # for i in edges:
    #     if 1 in i:
    #         L1.append(i)
    # L2 = []
    # for i in L1:
    #     L2.append(list(i))
    # L3 = []
    # for i in L2:
    #     for j in i:
    #         L3.append(j)
    # L4 = list(set(L3))
    # L5 = []
    # for i in L4:
    #     for j in edges:
    #         if i in j:
    #             L5.append(j)
    # L6 = []
    # for i in L5:
    #     for j in i:
    #         L6.append(j)
    # L6 = list(set(L6))
    # if 1 not in L6:
    #     L6.append(1)
    # a = len(L6)
    # return
    dict_pair = {}
    for v in range(1, n+1):
        dict_pair[v] = []
    for (v,w) in edges:
        dict_pair[v].append(w)
        dict_pair[w].append(v)
    visited = {}
    for v in range(1, n+1):
        visited[v] = False
    def P2_help(visited, v, count, dict_pair):
        if not visited[v]:
            visited[v] = True
            count = count +1
            for w in  dict_pair[v]:
                P2_help(visited, v, count, dict_pair)
    count = 0
    for v in range(1, n+1):
        P2_help(visited, v, count, dict_pair)
    return count


P2(7, [(1, 2), (2,3), (1,5), (5, 2), (5, 6), (4, 7)])
P2(1, [])
P2(3, [(1,2)])
P2(4, [(1, 2), (2, 1)])
P2(5, [(1,2), (2,3), (3,4), (4,5)])
