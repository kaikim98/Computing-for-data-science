from BST_Helper import *
def P1(root: TreeNode, low: int, high: int) -> int:     
    add = 0
    q = [root]
    if q == None:
        return []
    while q:
        curNode = q.pop()
        if low <= curNode.val <= high:
            add = add + curNode.val
            if curNode.right != None:
                q.append(curNode.right)
            if curNode.left != None:
                q.append(curNode.left)
        elif curNode.val < low:
            if curNode.right != None:
                q.append(curNode.right)
        elif curNode.val > high:
            if curNode.left != None:
                q.append(curNode.left)
    return add