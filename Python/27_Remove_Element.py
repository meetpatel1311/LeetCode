class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = []
        if(nums):
            for i in range(0,len(nums)):
                rec = nums[i]
                if(rec==val):
                    l.append(i)
        if(l):
            for rec in l[::-1]:
                del nums[rec]
            
        return len(nums)
            
