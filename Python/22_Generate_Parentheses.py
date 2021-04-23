from itertools import permutations
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backt(s,left,right):
            if(len(s)==2*n):
                ans.append(s)
                return 
            if(left<n):
                backt(s+'(',left+1,right)
            if(right<left):
                backt(s+')',left,right+1)
        backt("",0,0)
        return ans
