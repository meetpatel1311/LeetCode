class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = ""
        b = ""
        l1_len = 0
        l2_len=0
        while(l1):
            a = a + str(l1.val)
            l1_len+=1
            l1 = l1.next
        while(l2):
            b=b+str(l2.val)
            l2_len+=1
            l2 = l2.next
        a = int(a[::-1]) + int(b[::-1])
        a_str = str(a)[::-1]
        temp  = len(a_str)
        x=ListNode(int(a_str[-1]),None)
   
        for i in range(-2,0-temp-1,-1):
            x = ListNode(int(a_str[i]),x)
        return x
