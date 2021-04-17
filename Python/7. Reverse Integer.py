class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        x_abs = abs(x)
        st = str(x_abs)
        st = st[::-1]
        num = int(st)
        if(num<-2**31 or num>(2**31)+1):
            return 0
        elif(s[0]=='-'):
            return 0-num
        else:
            return num
        
