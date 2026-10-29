class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # check row
        seen = set()
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] in seen:
                    return False
                seen.add(board[row][col])
            seen.clear()

        # check col
        for col in range(9):
            for row in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] in seen:
                    return False
                seen.add(board[row][col])
            seen.clear()

       # square
        for i in range(3):
            for j in range(3):
                # checking subgrid...
                for cell_row in range(i*3, i*3+3):
                    for cell_col in range(j*3, j*3+3):

                        # check if it makes board valid
                        if board[cell_row][cell_col] == ".":
                            continue
                        if board[cell_row][cell_col] in seen:
                            return False
                        seen.add(board[cell_row][cell_col])

                # clear after each subgrid
                seen.clear()
        
        return True

                        
