class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if(board):
            r = []
            c = []
            box = []
            d ={}
            for i in range(9):
                r.append(d.copy())
                c.append(d.copy())
                box.append(d.copy())
            # print(type(r[0]),c)
            for i in range (0,9):
                for j in range(0,9):
                    temp = board[i][j]
                    if(temp !='.'):
                        temp = int(temp)
                        box_index = (i//3)*3 + j//3
                        if(temp in r[i].keys() or temp in c[j].keys() or temp in box[box_index].keys()):
                            return False
                        else:
                            r[i][temp] = temp
                            c[j][temp] = temp
                            box[box_index][temp] = temp
            return True
