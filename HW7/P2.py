def P2(lst):
    for x in reversed(range(len(lst))):
        for i in range(x):
            if len(lst[i]) > len(lst[i+1]):
                lst[i], lst[i+1] = lst[i+1], lst[i]
    for x in reversed(range(len(lst))):
        for i in range(x):
            if len(lst[i]) == len(lst[i+1]):
                if lst[i] > lst[i+1]:
                    lst[i], lst[i+1] = lst[i+1], lst[i]
    return lst