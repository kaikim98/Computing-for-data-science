def P5(lst):
    n = len(lst)
    for i in range(1,n+1):
        if lst.index(i) < lst.index(i+1):
            continue
        elif lst.index(i) > lst.index(i+1):
            a = i
            break
    b = n - a
    return b