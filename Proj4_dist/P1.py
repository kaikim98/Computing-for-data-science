#import os
#os.chdir('C:\\Users\\user\Desktop\김동현\수업\데사컴\Computing-for-data-science\Proj4_dist')

from BST_Helper import *
def P1(root: TreeNode, low: int, high: int) -> int:     
    add = 0
    if root == None:
        return 0
    q = [root]
    change = True
    while change:
        a = q.pop(0)
        if len(q) != 0:
            if low < a.left.val < high:
                add = add+ a.left.val
                print(a.left.val)
        elif len(q) == 0:
            change = False
    return add


root = create_linked_bst([10,5,15,3,7, 9, 18])
P1(root, 3, 9)
