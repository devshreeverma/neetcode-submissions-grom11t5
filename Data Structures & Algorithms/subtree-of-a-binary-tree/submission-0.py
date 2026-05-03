# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        ans=[]
        def inorder(node):  
            if not node:
                return '#'
            left=inorder(node.left)
            right=inorder(node.right)
            key=str(node.val)+','+left+','+right
            return key
        main=inorder(root)
        sub=inorder(subRoot)
        return sub in main

        