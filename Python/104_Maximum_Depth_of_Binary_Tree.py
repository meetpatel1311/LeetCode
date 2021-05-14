# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if(root is None):
            return 0
        def recurs(root,i,l):
            if(root):
                l[-1] = max(l[-1],i)
                recurs(root.left,i+1,l)
                recurs(root.right,i+1,l)
        l=[0]
        recurs(root,1,l)
        return l[-1]
