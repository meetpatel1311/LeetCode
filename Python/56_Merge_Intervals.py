class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        if(intervals):
            intervals.sort(key=lambda x:x[0])
            while(intervals):
                first = intervals.pop(0)
                temp_i=first[0]
                temp_j=first[1]
                while(intervals and intervals[0][0]<=temp_j):
                    second = intervals.pop(0)
                    temp_i = min(temp_i,second[0])
                    temp_j=max(temp_j,second[1])
                ans.append([temp_i,temp_j])
            return ans
            
            
        else:
            return []
        
