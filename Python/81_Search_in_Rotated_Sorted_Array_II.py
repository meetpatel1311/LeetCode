class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # nums = [2,5,6,0,0,1,2]
        # target = 3
        def mine(l,h,nums,target):
            if(h>=l):
                mid = (l+h)//2
                if(nums[mid]==target):
                    return True
                elif(nums[mid]>target):
                    return mine(l,mid-1,nums,target)
                else:
                    return mine(mid+1,h,nums,target)
                    
            else:
                return False
        x=False
        for i in range(1,len(nums)):
            if(nums[i]<nums[i-1]):
                x=True
                break
        if(x):
            return True if(mine(0,i-1,nums,target) or mine(i,len(nums)-1,nums,target)) else False
        else:
            return mine(0,len(nums)-1,nums,target)
        
