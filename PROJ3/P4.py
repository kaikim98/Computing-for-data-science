def P4(nums):
    L1 = []
    for i in nums:
        if i+1 in nums:
            L1.append([i, i+1])
        else:
            continue
    L1.sort(key=lambda x:x[0])
    x = len(L1)-1
    count = 0
    L3 = []
    for a in range(x):
        if L1[a][1] == L1[a+1][0]:
            count = count + 1
            L3.append(count)
        else:
            count = 0
    if len(L3) == 0:
        return 1
    y = max(L3)+2
    return y