"""
Implement a function that takes a list of integers as its input argument 
and returns a set of those integers occurring two or more times in the list.


>>>P1([1,2,3,1])
{1}

>>>P1([1,2,3,4])
set()

>>>P1([])
set()

>>> P1([1,2,3,1,4,2])
set({1,2})
"""


def P1(L1):
    L2 = []
    for i in L1:
        if L1.count(i) > 1:
            L2.append(i)
    b = set(L2)
    return b