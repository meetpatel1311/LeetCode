class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=[]
        if(nums):
            el=nums[0]
            for i in range(1,len(nums)):
                rec=nums[i]
                if(rec==el):
                    l.append(i)
                else:
                    el=rec
        if(l):
            for rec in l[::-1]:
                del nums[rec]
