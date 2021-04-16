class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(s==''):
            return 0
        set_s = set()
        max_possible = len(s)
        current_max = 1
        
        for i in range(0,len(s)-1):
            
            set_s.clear()
            set_s.add(s[i])
            
            if(max_possible>current_max):
                
                for j in range(i+1,len(s)):
                    if(s[j] in set_s):
                        break
                    set_s.add(s[j])
                    
                if(len(set_s)>current_max):
                    
                    current_max = len(set_s)
                max_possible -=1
                
            else:
                break
                
        return current_max
                    
