# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def search_tree(self,t1,t2):
        if(t1==None and t2==None):
            return True
        if(t1==None or t2==None):
            return False
        return (t1.val==t2.val) and self.search_tree(t1.left,t2.right) and self.search_tree(t1.right,t2.left)
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.search_tree(root,root)
    
