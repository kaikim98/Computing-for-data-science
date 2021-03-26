"""
Practical programming Chapter 8 Exercise 7  

**Instruction**
Precondition: len(L) >= 2
Return True if and only if first item of the list is the same as the last.
>>> P1([3, 4, 2, 8, 3])
True
>>> P1(['apple', 'banana', 'pear'])
False
>>> P1([4.0, 4.5])
False

Complete P1 function
"""

def P1(L: list) -> bool:
    if L[0]==L[-1]:
        return True
    else:
        return False