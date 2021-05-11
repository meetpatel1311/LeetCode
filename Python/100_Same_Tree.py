# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        stack,output1,output2 = [p,],[],[]
        while(stack):
            node = stack.pop()
            if node is not None:
                output1.append(node.val)
            else:
                output1.append(None)
            if node is not None:
            # if(node.right):
                stack.append(node.right)
            # if(node.left):
                stack.append(node.left)
        stack = [q,]
        while(stack):
            node = stack.pop()
            if node is not None:
                output2.append(node.val)
            else:
                output2.append(None)
            if node is not None:
            # if(node.right):
                stack.append(node.right)
            # if(node.left):
                stack.append(node.left)
        return True if output1 == output2 else False
