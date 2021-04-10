def P1(path: str) -> str:        
    L1 = []
    n = len(path)
    for i in range(1,n-1):
        if path[i] == '/' and path[i+1] == '/':
            continue
        elif path[i] == '.':
            if path[i+1] != '.':
                continue
            if path[i+1] == '.':
                if i < n-2:
                    if path[i+2] != '.':
                        if len(L1) == 0:
                            continue
                        else:
                            b = "".join(L1)
                            a = b.rfind('/')
                            del L1[a+1:]
                elif i == n-2:
                    if len(L1) == 0:
                        continue
                    else:
                        b = "".join(L1)
                        a = L1.rfind('/')
                        del L1[a+1:]
                else:
                    continue
        elif path[i] == '/' and path[i-1] == '.':
            continue
        elif path[i] == ',' and path[i+1] == '/':
            continue
        else:
            L1.append(path[i])
    L1.insert(0, '/')
    str1 = "".join(L1)
    return str1

P1('/../')
P1('/home//foo/')
P1('/home/')
P1('/a/./b/../../c/')
