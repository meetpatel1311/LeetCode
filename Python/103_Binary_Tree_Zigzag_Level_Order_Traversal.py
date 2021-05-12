# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if(root):
            l=[]
            curr = [root]
            while(curr):
                m=[]
                temp = []
                while(curr):
                    
                    t = curr.pop()
                    temp.append(t)
                    m.append(t.val)
                temp.reverse()
                for rec in temp:
                    if(rec.right):
                        curr.append(rec.right)
                    if(rec.left):
                        curr.append(rec.left)
                    
                l.append(m.copy())
            print(l)
            for i in range(1,len(l),2):
                l[i].reverse()
            return l
            
            
        return []
