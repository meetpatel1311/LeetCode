class Solution:
    def romanToInt(self, s: str) -> int:
        d1 = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        d2={'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        ans=0
        for rec in d2:
            if(rec in s):
                s=s.replace(rec,'')
                ans = ans + d2[rec]
        for rec in s:
            ans+=d1[rec]
        return ans
