# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth=1
        def dep(node):
            if not node:
                return 0
            d1,d2=0,0
            left=dep(node.left)
            right=dep(node.right)
            return 1+max(left,right)
        return dep(root)

    