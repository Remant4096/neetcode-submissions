class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map = [[0]*9 for _ in range(9)]
        col_map = [[0]*9 for _ in range(9)]
        box_map = [[0]*9 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                val = board[i][j]

                if(val == '.'):
                    continue
                
                val = int(val)

                if(row_map[i][val-1]):
                    return False

                if(col_map[j][val-1]):
                    return False

                if(box_map[3*(i//3) + j//3][val-1]):
                    return False
                
                row_map[i][val-1] = 1
                col_map[j][val-1] = 1
                box_map[3*(i//3) + j//3][val-1] = 1

        return True
