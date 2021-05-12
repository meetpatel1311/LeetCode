class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        stack = [root,]
        output=[]
        des = []
        if(root is None):
            return []
        while(stack):
            des=[]
            output.append([])
            while(stack):
                curr = stack[0]
                output[-1].append(curr.val)
                if(curr.left):
                    des.append(curr.left)
                if(curr.right):
                    des.append(curr.right)
                
                del stack[0]
            stack = des.copy()
        return output
