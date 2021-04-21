class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = 2**31
        nums.sort()
        ss = 0
        
        for i in range(len(nums)):
            if i == 0 or nums[i-1] != nums[i]:
                lo, hi = i+1, len(nums)-1
                while(lo<hi):
                    sum = nums[i]+ nums[lo]+ nums[hi]
                    t = abs(target - sum)
                    if(t<diff):
                        diff = t
                        ss = sum
                    if sum < target:
                        lo+=1
                    elif sum > target :
                        hi-=1
                    else:
                        return sum
        return ss
        
                
        
