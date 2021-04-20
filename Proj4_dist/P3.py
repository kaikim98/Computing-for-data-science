"""
**Instruction**
Please see instruction document.
"""
from BST_Helper import *
def P3(root: TreeNode, val: int) -> TreeNode:    
    q = [root]
    a = q.val
    while q:
        next_level = []
        for x in q:
            if x.left != None:
                next_level.append(x.left)
            if x.right != None:
                next_level.append(x.right)
            if x.left == None:
                
    return root