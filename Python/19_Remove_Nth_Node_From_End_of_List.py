class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if(head):
            i=0
            j=0
            prev = head
            curr=head
            x=True
            while(curr):
                curr=curr.next
                i+=1
                if(x==False):
                    j+=1
                if(i-j==n):
                    if(x):
                        x=False
                        prev=head
                    else:
                        prev_ = prev
                        prev=prev.next
            if(j==0):
                head = head.next
            else:
                prev_.next=prev.next
            return head
            
                
        return head
