class Solution(object):
    def generateMatrix(self, n):
        matrix = [[0 for _ in range(n)] for __ in range(n)]
        count=1
        def go_right(count,row,j,n):
            if(count>n**2):
                return
            while(j<n and matrix[row][j]==0):
                matrix[row][j]=count
                count+=1
                j+=1
                if(j==n):
                    # print(n)
                    break
            go_down(count,row+1,j-1,n)
        def go_down(count,i,col,n):
            if(count>n**2):
                return
            while(i<n and matrix[i][col]==0):
                matrix[i][col]=count
                count+=1
                i+=1
                if(i==n):
                    break
            go_left(count,i-1,col-1,n)
        def go_left(count,row,j,n):
            if(count>n**2):
                return
            while(j>=0 and matrix[row][j]==0):
                matrix[row][j]=count
                count+=1
                j-=1
                if(j<0):
                    break
            go_up(count,row-1,j+1,n)
        def go_up(count,i,col,n):
            if(count>n**2):
                return 
            while(i>=0 and matrix[i][col]==0):
                matrix[i][col]=count
                count+=1
                i-=1
                if(i<0):
                    break
            go_right(count,i+1,col+1,n)
        go_right(count,0,0,n)
        return matrix
