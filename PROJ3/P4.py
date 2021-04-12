def P4(nums):
    L1 = []
    n = len(nums)
    for i in nums:
        for j in range(1, n+1):
            if i+j in nums:
                L1.append(j)
            else:
                break
            
    if len(L1) == 0:
        return 1
    m = max(L1)+1
    return m

P4([3,6,4,64,10,29,5,9,11])
P4([-1, 5, 2, -6, 8])
P4([-3, 2, 0, 1, -2, -1])
