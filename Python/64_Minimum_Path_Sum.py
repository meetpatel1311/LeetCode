class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if(grid):
            r = len(grid)
            c = len(grid[0])
            if(r==1):
                return sum(grid[0])
            elif(c==1):
                ans = 0
                for rec in grid:
                    ans = ans + rec[0]
                return ans
            else:
                for i in range(1,c):
                    grid[0][i] = grid[0][i] + grid[0][i-1]
                for j in range(1,r):
                    grid[j][0] = grid[j][0] + grid[j-1][0]
                for i in range(1,r):
                    for j in range(1,c):
                        grid[i][j] = grid[i][j] + min(grid[i][j-1],grid[i-1][j])
                return grid[-1][-1]
                    
