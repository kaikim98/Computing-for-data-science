"""
A balanced color is one whose red, green, and blue values add up to 1.0. 
Implement a function that takes a dictionary whose keys are 'R', 'G', and 'B' 
and whose values are between 0 and 1 as input and that returns True 
if they represent a balanced color.


>>>P4({'R': 0.2, 'G': 0.3, 'B': 0.5})
True

>>>P4({'R': 0.2, 'G': 0.3, 'B': 0.6})
False

>>>P4({'R': 0.1, 'G': 0.1, 'B': 0.1})
False
"""


def P4(dct):
    a = dct.values()
    i = 0
    for num in a:
        i = i + num
    if i == 1:
        return True
    else:
        return False