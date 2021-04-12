def P1(nums, k):
    # L1 = []
    # for i in nums:
    #     a = i % k
    #     L1.append(a)
    # while len(L1) == 0:
    #     if L1[0] == 0:
    #         if 0 in L1[1:]:
    #             del L1[0]
    #             a = L1.index(0)
    #             del L1[a]
    #         if 0 not in L1[1:]:
    #             return False
    #             break
                
    #     elif L1[0] != 0:
    #         b = k - L1[0]
    #         if b in L1[1:]:
    #             del L1[0]
    #             a = L1.index(b)
    #             del L1[a]
                
    #         else:
    #             return False
    #             break
    # return True
    L1 = []
    L2 = []
    for i in nums:
        a = i % k
        L1.append(a)
    for i in L1:
        i

P1([123, 36, 54, 28, 39, 28], 2)
P1([123, 36, 54, 28, 39, 28], 3)
P1([3,7,6,5,4,5], 5)