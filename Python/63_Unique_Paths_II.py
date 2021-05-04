class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:

        r = len(grid)
        c = len(grid[0])
        if(grid[0][0]==1):
            return 0 
        grid[0][0]=1
        for i in range(1,r):
            if(grid[i-1][0]==1 and grid[i][0]==0):
                grid[i][0] = 1  
            else:
                grid[i][0]= 0
            
        for j in range(1,c):
            if(grid[0][j-1]==1 and grid[0][j]==0):
                grid[0][j] = 1 
            else:
                grid[0][j] = 0
        for i in range(1,r):
            for j in range(1,c):
                if(grid[i][j]==0):
                    grid[i][j]=grid[i-1][j]+grid[i][j-1]
                else:
                    grid[i][j]=0
        return grid[-1][-1]
