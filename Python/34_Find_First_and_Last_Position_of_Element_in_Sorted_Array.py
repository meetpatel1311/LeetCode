class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        c = nums.count(target)
        if(c==0):
            return [-1,-1]
        ind = nums.index(target)
        l=[]
        # if(c==1):
        #     l.append(ind)
        #     l.append(ind)
        #     return l
        l.append(ind)
        for i in range(1,c):
            ind+=1
        l.append(ind)
        
        
        return l
