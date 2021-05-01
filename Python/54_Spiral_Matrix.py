class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans=[]
        
        def delete_first_row(matrix,n,ans):
            ans.extend(matrix.pop(n))
            
        def delete_last_row(matrix,n,ans):
            l = matrix.pop(n)
            l.reverse()
            ans.extend(l)
            
        def delete_last_column(matrix,n,ans):
            for i in range(len(matrix)):
                ans.append(matrix[i].pop(n))
            check(matrix)
            
        def delete_first_column(matrix,n,ans):
            l=[]
            for i in range(len(matrix)):
                l.append(matrix[i].pop(n))
            l.reverse()
            ans.extend(l)
            check(matrix)
            
        def check(matrix):
            l=[]
            for i in range(0,len(matrix)):
                if(matrix[i]==[]):
                    l.append(i)
            l.reverse()
            for rec in l:
                matrix.pop(rec)
                
        while(matrix):
            if(matrix):
                delete_first_row(matrix,0,ans)
            else:
                break
            if(matrix):
                delete_last_column(matrix,len(matrix[0])-1,ans)
            else:
                break
            if(matrix):
                delete_last_row(matrix,len(matrix)-1,ans)
            else:
                break      
            if(matrix):
                delete_first_column(matrix,0,ans)
            else:
                break
        return ans
