class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_ = 0
        l=0
        r = len(height)-1
        while(l<r):
            first = height[l]
            second = height[r]
            temp = min(first,second)
            area = temp*(r-l)
            if(area>max_):
                max_ = area
            if(first<second):
                l+=1
            else:
                r-=1
        return max_
