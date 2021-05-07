class Solution:
    def mySqrt(self, x: int) -> int:
        i=0
        while(True):
            if(x<i**2):
                break
            i+=1
        return i-1
