class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        l = [[1 for j in range(n)] for i in range(m)]
        
        for i in range(1,m):
            for j in range(1,n):
                l[i][j] = l[i][j-1]+l[i-1][j]
        return l[m-1][n-1]
            
        
        
        
                
        
