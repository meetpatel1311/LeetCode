class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if(head):
            curr = head
            l = [curr.val]
            while(curr.next):
                temp_ = curr.next
                if(temp_.val in l):
                    curr.next = temp_.next


                else:
                    l.append(temp_.val)
                    curr = curr.next
            return head
