class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if(s):
            la = []
            c = 0
            for rec in s:
                if(rec == " "):
                    la.append(c)
                    c= 0
                else:
                    c= c+1
            la.append(c)
            for i in range(la.count(0)):
                la.remove(0)
            if(la):
                return la[-1]
            else:
                return 0
        else:
            return 0
