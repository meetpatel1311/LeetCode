class Solution:
    def convert(self, s: str, n: int) -> str:
        l = ["" for i in range(n)]
        if(s and n>0):
            len_s = len(s)
            if(n==1):
                return s
            elif(n==2):
                t = ""
                for i in range(0,len_s,2):
                    t=t+s[i]
                for i in range(1,len_s,2):
                    t = t+s[i]
                return t
            i=0
            while(i<len_s):
                temp = 0
                if(i+n<=len_s):
                    
                    for j in range(i,i+n):
                        l[temp] = l[temp]+s[j]
                        temp = temp +1
                    i = i+n
                else:
                    for j in range(i,len_s):
                        l[temp] = l[temp] + s[j]
                        temp = temp + 1
                    break
                temp = -2
                if(i+n-2<=len_s):
                    for j in range(i,i+n-2):
                        l[temp] = l[temp] + s[j]
                        temp = temp - 1
                    i = i+n-2
                else:
                    for j in range(i,len_s):
                        l[temp] = l[temp] + s[j]
                        temp = temp -1
                    break
            return "".join(l)                                                             
        return ""
        
