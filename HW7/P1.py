def P1(lst):
    lst_copy = sorted(lst)
    n = len(lst)
    count = 0
    while True:
        if lst == lst_copy:
            break
        elif lst != lst_copy:
            for i in range(n-1):
                if lst[i] > lst[i+1]:
                    count += 1
                    lst[i], lst[i+1] = lst[i+1], lst[i]
                    break
                elif lst[i] < lst[i+1]:
                    continue
    return count