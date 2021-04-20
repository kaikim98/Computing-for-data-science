from BST_Helper import *
def P2(root: TreeNode):
    q = [root]
    L1 = []
    while q:
        next_level = []
        L2 = []
        for x in q:
            L2.append(x.val)
            if x.left != None:
                next_level.append(x.left)
            if x.right != None:
                next_level.append(x.right)
        q = next_level
        L1.append(L2)
    L3 = list(reversed(L1))
    return L3