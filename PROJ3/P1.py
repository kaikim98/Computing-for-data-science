def P1(nums, k):
    L1 = []
    for i in nums:
        a = i % k
        L1.append(a)
    for i in L1:
        if i == 0:
            if L1.count(0) % 2 == 0:
                continue
            else:
                return False
        else:
            if L1.count(i) == L1.count(k - i):
                continue
            else:
                return False
            
    return True