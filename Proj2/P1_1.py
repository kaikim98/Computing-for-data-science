L1 = ['ab', 'bc', 'cd', 'de', 'asdf', 'asd', 'qwr', 'qwdffa', 'jikj']
del L1[2:]
print(L1)


def P1(path: str) -> str:  
    a = path.split('/')
    L1 = []
    for i in range(1, len(a)):
        if a[i] == '/' and a[i+1] == '/':
            continue
        if a[i] == '.':
            continue
        if a[i] == '..':
            if len(L1) == 0:
                continue
            else:
                del L1[-2:-1]
        else:
            L1.append(a[i])
            L1.append('/')
            
    L1.insert(0, '/')
    str1 = "".join(L1)
    return str1