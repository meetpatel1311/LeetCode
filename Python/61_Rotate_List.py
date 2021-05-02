# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if(head and k>0):
            curr = head 
            l = 0
            while(curr):
                l=l+1
                curr = curr.next
            if(l==1):
                return head
            num = k%l
            mine = l-num
            if(mine==l):
                return head
            curr= head
            temp = 0
            f = curr
            # return curr

            while(temp<mine):
                temp+=1
                if(temp==mine):
                    ans = curr.next
                    curr.next = None
                    temp = ans
                    if(ans.next):
                        while(ans.next):
                            ans = ans.next
                    ans.next = f
                    return temp
                curr = curr.next
            return head
        return head
            
            
