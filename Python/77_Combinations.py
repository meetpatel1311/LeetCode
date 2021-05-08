from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if(k==0):
            return []
        elif(k==1):
            ans = [[i] for i in range(1,n+1)]
            return ans
        else:
            l = [i for i in range(1,n+1)]
            ans = []
            c = combinations(l,k)
            for rec in c:
                ans.append(list(rec))
            return ans            
            
        
