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