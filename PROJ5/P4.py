def P4(L, T):
    count = 0
    L = int(L)
    T = int(T)
    change = True
    if L > T:
        return L - T
    elif L == T:
        return 0
    else:
        while change:
            if 2*L < T:
                L = 2*L
                count = count + 1
                print('a')
            elif 2*L > T:
                # if T - L > L :
                a = T - L
                if a % 2 == 1:
                    count = count + int(a/2) +1
                    print('x')
                    change = False
                else:
                    count = count + a/2
                    print('y')
                    change = False
                # elif T - L < L:
                #     count = count + T- L
                #     print('y')
                #     change = False
    return count      
P4(5, 17)
P4(123, 12345)
