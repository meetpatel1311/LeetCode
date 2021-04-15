class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = nums.copy()
        nums.sort()
        len_nums = len(nums)
        l=0
        r=len_nums-1
        while(l<r):
            temp_sum = nums[l] + nums[r]
            if(temp_sum==target):
                if(nums[l]==nums[r]):
                    ind1 = ans.index(nums[r])
                    ind2 = ans[ind1+1::].index(nums[r])+ind1+1
                    return [ind1,ind2]
                else:
                    return [ans.index(nums[l]),ans.index(nums[r])]
            elif(temp_sum<target):
                l=l+1
            else:
                r=r-1
