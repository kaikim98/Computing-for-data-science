"""
**Instruction**
<Factor into two prime numbers>
Input of P2 function is natural number.
P2 function returns whether the input nubmer could be factored into two prime numbers.
Do not worry about invalid input.

>>> P2(6) #2 * 3
True

>>> P2(9) #3 * 3
True

>>> P2(12) # 2 * 2 * 3
False

>>> P2(7) # 7
False


"""
def P2(n:int) -> bool:
    count = 0
    L1 =[]
    for i in range(2, int(n/2 +1)):
        count += 1
        if n % i != 0:
            continue
        if n % i == 0:
            a = n / i
            L1.append(a)
            break
    if len(L1) == 0:
        return False
    for j in range(2, int(a/2 +1)):
        if a % j != 0:
            continue
        if a % j == 0:
            return False
            break
    return True