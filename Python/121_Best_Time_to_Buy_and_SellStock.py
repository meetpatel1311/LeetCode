class Solution:
    def maxProfit(self, p: List[int]) -> int:
        ans = [0]
        # print(max(ans))
        if(p):
            min_ = max(p)
            for i,rec in enumerate(p,0):
                min_ = min(rec,min_)
                ans.append(max(ans[-1],rec-min_))
        return ans[-1]
