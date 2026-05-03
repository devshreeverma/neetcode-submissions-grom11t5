# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def same(nodep,nodeq):
            if not nodep:
                if not nodeq:
                    return True
                else:
                    return False
            if not nodeq:
                if not nodep:
                    return True
                else:
                    return False
            if nodep.val==nodeq.val:
                return same(nodep.left,nodeq.left) and same(nodep.right,nodeq.right)
            else:
                return False
        return same(p,q)
                