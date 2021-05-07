class Solution:
    def climbStairs(self, n: int) -> int:
        
        ans = [0,1,2]
        for i in range(3,n+1):
            ans.append(ans[-1]+ans[-2])
        return ans[n]
