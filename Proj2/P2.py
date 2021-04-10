def P2(parentheses: str) -> bool:        
    L1 = []
    for i in parentheses:
        if i == '(':
            L1.append('a')
        if i == '{':
            L1.append('b')         
        if i == '[':
            L1.append('c')
        if i == ')':
            if L1[-1] == 'a':
                del L1[-1]
            else:
                return False
        if i == '}':
            if L1[-1] == 'b':
                del L1[-1]
            else:
                return False
        if i == ']':
            if L1[-1] == 'c':
                del L1[-1]
            else:
                return False
    if len(L1) == 0:
        return True
    else:
        return False