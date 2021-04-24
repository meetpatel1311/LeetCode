class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        if(head):
            curr = head
            l = []
            while(curr):
                l.append(curr)
                curr = curr.next
            x=None
            if(len(l)%2==1):
                x = l.pop()
            if(l):
                while(l):
                    l[-2].next = x
                    l[-1].next = l[-2]
                    x=l[-1]
                    l.pop()
                    l.pop()
            else:
                return head
            return x
        return head
