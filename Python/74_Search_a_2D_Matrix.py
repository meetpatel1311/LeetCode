class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def perfectmatricsearch(i,matrix,target,r,c):
            for temp in range(0,i+1):
                if(matrix[i][temp]==target or matrix[temp][i]==target):
                    return True
            return sub(i,r,c,matrix,target)
        def sub(i,r,c,matrix,target):
            for temp in range(0,i):
                if(target<=matrix[temp][-1]):
                    for k in range(i+1,c):
                        if(matrix[temp][k]==target):
                            return True
                    break
            return False
        if(matrix):
            # target=50
            r = len(matrix)
            c = len(matrix[0])
            min_ = min(r,c)
            if(r==1 and c==0):
                return False
            for i in range(0,min_):
                if(matrix[i][i]==target):
                    return True
                elif(matrix[i][i]>target):
                    return perfectmatricsearch(i,matrix,target,r,c)
            if(r<c):
                for j in range(i+1,c):
                    # print(matrix[i][j])
                    if(target==matrix[i][j]):
                        return True
                    elif(target<matrix[i][j]):
                        for row in range(0,r):
                            if(matrix[row][j]==target):
                                return True
                        return False
            elif(r>c):
                for row in range(i+1,r):
                    if(target<=matrix[row][-1]):
                        if(target==matrix[row][-1]):
                            return True
                        for j in range(0,c):
                            if(matrix[row][j]==target):
                                return True
                        return False
                
                
            return False
                
        return False    
