"""
Practical programming Chapter 9 Exercise 12

**Instruction**
When P5([1, 2, 3, -3, 6, -1, -3, 1]) is executed, it produces [1, 2, 3, 6, -3, 1].
The for loop traverses the elements of the list, and when a negative value
(like -3 at position 3) is reached, it is removed, shifting the subsequent
values one position earlier in the list (so 6 moves into position 3). The
loop then continues on to process the next item, skipping over the value
that moved into the removed item’s position. If there are two negative
numbers in a row (like -1 and -3), then the second one won’t be removed.
Rewrite the code to avoid this problem.
Assume each element of input list is always number.

Remove the negative numbers from the list num_list.
>>> numbers = [-5, 1, -3, 2]
>>> P5(numbers)
>>> numbers
[1, 2]
  
"""
from typing import List
def P5(num_list: List[float]) -> List[float]:
    L1 = num_list
    for j in num_list:
        if j < 0:
            num_list.remove(j)
    a = len(L1)
    for m in range(0,a-1):
        if L1[m]<0 and L1[m+1]<0:
            add = m+1
            x= 0
            for n in range(0,add):
                if n < 0:
                    x = x+1
            num_list.insert(m+1-x, L1[m+1])
        else:
            return num_list