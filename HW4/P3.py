"""
Implement a function that takes a dictionary as an argument
and returns the number of values that appear two or more times.

* Condition: All values are hashable.


>>>P3({'red': 1, 'green': 1, 'blue': 2})
1

>>>P3({'r': 'a', 'g': 'b', 'b': 'c'})
0

>>>P3(dict())
0

>>>P3({'a':True, 'b': True, 'c':2, 'd':2})
2
"""

def P3(dct):
    L1 = []
    L2 = []
    a = dct.values()
    for value in a:
        L1.append(value)
    for i in L1:
        if L1.count(i) > 1:
            L2.append(i)
    b = len(set(L2))
    return b