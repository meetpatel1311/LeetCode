class Solution:
    def longestPalindrome(self, s: str) -> str:
        len_s = len(s) 
        if(s == s[::-1]):
            return s
        for i in range(1,len(s)):
            for j in range(0,i):
                f = s[j:j+len_s]
                se = f[::-1]
                if(f==se):
                    return f
            len_s-=1
        return s[0]
            
