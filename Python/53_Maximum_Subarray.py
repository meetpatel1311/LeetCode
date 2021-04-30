class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if(nums):
            max_ = min(nums) 
            sum_ = 0
            for rec in nums:
                sum_ = max(rec,sum_+rec)
                max_ = max(sum_,max_)
            return max_
        else:
            return 0
        
