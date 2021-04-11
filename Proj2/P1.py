L1 = ['ab', 'bc', 'cd', 'de', 'asdf', 'asd', 'qwr', 'qwdffa', 'jikj']
L1.insert(0,'/')
print(L1)


def P1(path: str) -> str:  
    a = path.split('/')
    b = list(filter(None, a))
    L1 = []
    for i in range(0, len(b)):
        if b[i] == '/' and b[i+1] == '/':
            continue
        if b[i] == '.':
            continue
        if b[i] == '..':
            if len(L1) == 0:
                continue
            else:
                del L1[-2:]
        else:
            L1.append(b[i])
            L1.append('/')
            
    L1.insert(0, '/')
    if len(L1) > 1 and L1[-1] == '/':
        del L1[-1]
    str1 = "".join(L1)
    return str1