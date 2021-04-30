import heapq
class Solution(object):
    ans = []
    def isitsafe(self,board,qsf,col,n):
        for j in range(0,qsf):
            if(board[j][col]=='Q'):
                return False
        i=qsf-1
        j=col-1
        while(i>=0 and j>=0):
            if(board[i][j]=='Q'):
                return False
            i-=1
            j-=1
        i=qsf-1
        j=col+1
        while(i>=0 and j<n):
            if(board[i][j]=='Q'):
                return False
            i-=1
            j+=1
        return True
    def mine(self,n,board,qsf):
        if(qsf==n):
            temp=[]
            for rec in board:
                temp.append("".join(rec))
            self.ans.append(temp[:])
        
        for c in range(n):
            if(self.isitsafe(board,qsf,c,n)):
                board[qsf][c]='Q'
                self.mine(n,board,qsf+1)
                board[qsf][c]='.'
                
                
    def solveNQueens(self, n):
        qsf = 0
        board = [['.' for i in range(n)] for j in range(n)]
        self.ans=[]
        self.mine(n,board,qsf)
        
        return self.ans
        
