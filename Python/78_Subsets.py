from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        temp = []
        final = []
        for i in range(0,len(nums)):
            temp.extend(combinations(nums,i+1))
        for rec in temp:
            final.append(list(rec))
        final.append([])
        return final
