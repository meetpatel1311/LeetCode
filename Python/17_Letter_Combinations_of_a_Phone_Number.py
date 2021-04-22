from itertools import product
class Solution:
    def letterCombinations(self, digits):
        d = {'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        if(digits):
            len_digits = len(digits)
            if(len_digits==1):
                return d[digits]
            ans = list(d[digits[0]])
            
            for i in range(1,len_digits):
                ans = list(product(ans,d[digits[i]]))
                for i,rec in enumerate(ans):
                    s=''
                    ans[i] = s.join(rec)
            return ans 
