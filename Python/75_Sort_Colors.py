class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0 
        while(i<len(nums)):
            if(nums[j]==0):
                nums.insert(nums.pop(j),0)
                j+=1
            elif(nums[j]==1):
                j+=1
            else:
                nums.append(nums.pop(j))
            i+=1
