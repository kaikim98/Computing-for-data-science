def P1(nums, k):
    L1 = []
    for i in nums:
        a = i % k
        L1.append(a)
    for i in L1:
        if i == 0 and L1.count(0) %2 ==0:
            continue
        elif i !=0 and L1.count(i) == L1.count(k-1):
            continue
        else:
            return False
    return True