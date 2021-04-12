def P2(nums):
    x = len(nums)
    a = int(len(nums)/2)
    L1 = []
    for i in range(1, a+1):
        for j in range(x-2*i+2):
            if nums[j:j+2*i+1].count(0) == i:
                L1.append(2*i)
    if len(L1) == 0:
        return 0
    m = max(L1)
    
    return m