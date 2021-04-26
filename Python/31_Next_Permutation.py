class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        x=False
        if(len_nums==1):
            return nums
        for i in range(-1,-len_nums,-1):
            if(nums[i]>nums[i-1]):
                for j in range(-1,i-1,-1):
                    if(nums[i-1]<nums[j]):
                        nums[i-1],nums[j] = nums[j],nums[i-1]
                        x=True
                        for m in range(i,-1):
                            for n in range(m+1,0):
                                if(nums[m]>nums[n]):
                                    nums[m],nums[n] = nums[n],nums[m]
                        break
                if(x):
                    break
        if(x==False):
            nums.sort()
        
