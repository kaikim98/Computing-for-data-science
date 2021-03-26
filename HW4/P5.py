"""
Implement a function that takes two dictionaries as arguments
and returns a dictionary that contains only the key/value pairs found in both
of the original dictionaries.


>>>P5({'a': 1, 'b':True, 'c':[1,2]}, {'a':1, 'b':123, 'c':[1,2]})
{'a': 1, 'c': [1, 2]}

>>>P5({'a': 1, 'b':True }, {'c':1, 'd':123, 'e':[1,2]})
{}

>>>P5({}, {'c':1, 'd':123, 'e':[1,2]})
{}

"""
def P5(dct1, dct2):
    a = []
    L1 = []
    L2 = {}
    b = dct2.keys()
    c = dct1.keys()
    d = []
    for i in b:
        a.append(i)
    for m in c:
        d.append(m)
    for key in a:
        if key in d:
            if dct1[key] == dct2[key]:
                L1.append(key)
            elif dct1[key] != dct2[key]:
                continue
        else:
            continue
    for j in L1:
        L2[j] = dct1[j]
    return L2