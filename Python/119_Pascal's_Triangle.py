class Solution:
    def getRow(self, n: int) -> List[int]:
        ans=[[1],[1,1],[1,2,1]]
        # n=33
        if(n>=0 and n<=2):
            return ans[n]
        for i in range(3,n+1):
            temp=[1]
            for j in range(1,len(ans[i-1])):
                
                temp.append(ans[i-1][j]+ans[i-1][j-1])
            temp.append(1)
            ans.append(temp[:])
        return ans[n]
        
