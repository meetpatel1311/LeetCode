class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ''
        for rec in s:
            if(rec.isalnum()):
                st = st + rec
        st = st.lower()
        if(st == st[::-1]):
            return True
        else:
            return False
        
