class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        def block_incorrect(block: list) -> bool:
                    mask = [False]*9
                    for val in block:
                        if(val == '.'):
                            continue
        
                        if(mask[int(val) -1]):
                            return True
                        mask[int(val) -1] = True
                    return False
        
        for row in board:
            if(block_incorrect(row)):
                return False

        for i in range(9):
            col = [board[j][i] for j in range(9)]
            if(block_incorrect(col)):
                return False

        i,j = 0,0

        while(i < 9):
            j = 0
            while(j < 9):
                block = list()
                for it in range(3):
                    for jt in range(3):
                        block.append(board[i + it][j + jt])

                j = j + 3  
                if(block_incorrect(block)):
                     return False
            i = i + 3

        return True