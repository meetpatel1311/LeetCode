class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # nums = [0,2,2,1,1]
        nums = list(set(nums))
        nums.append(1)
        
        len_nums = len(nums)
        nums.sort()
        temp = 1
        for i in range(nums.index(1)+1,len_nums):
            if(nums[i]!=temp):
                return temp
            temp = temp +1
        return temp
