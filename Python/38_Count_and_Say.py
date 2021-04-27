from collections import OrderedDict
class Solution:
    def countAndSay(self, n: int) -> str:
        d = OrderedDict({1:'1',2:'11',3:'21',4:'1211',5:'111221'})
        if(n in d.keys()):
            return d[n]
        else:
            for i in range(6,n+1):
                temp = d[i-1]+"_"
                t = temp[0]
                ans = ''
                c=1
                for j in range(1,len(temp)):
                    if(temp[j]==t):
                        c=c+1
                    else:
                        ans = ans + str(c)+ t
                        c=1
                        t=temp[j]
                d[i] = ans
            return d[n]
