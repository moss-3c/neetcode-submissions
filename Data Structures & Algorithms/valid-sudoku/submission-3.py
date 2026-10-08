# Solution 1 but row+col checking done at the same time
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
         # O(n) space - sets have at most n values
        row_dupes = set()
        col_dupes = set()

        # check all rows are valid O(n^2)
        for i in range(9):
            for j in range(9):
                # checking single row
                row_digit = board[i][j]
                col_digit = board[j][i]
                if self.digitAlreadyExists(row_dupes, row_digit):
                    return False
                if self.digitAlreadyExists(col_dupes, col_digit):
                    return False
            # clear dupes after checking each row
            row_dupes.clear()
            col_dupes.clear()

        # check all subgrids are valid O(n^2)
        # loop through subgrids: index 0, 3, 6
        dupes = set()

        for row_offset in (range(0, 9, 3)):
            for col_offset in (range(0, 9, 3)):

                # check subgrid is valid
                for i in range(row_offset, row_offset + 3):
                    for j in range(col_offset, col_offset + 3):
                        digit = board[i][j]
                        if self.digitAlreadyExists(dupes, digit):
                            return False
                
                # clear dupes after checking each subgrid
                dupes.clear()
        
        return True


    def digitAlreadyExists(self, dupes, digit: int) -> bool:
        # if cell is not blank
        if digit == '.':
            return False
        else:
            # if digit is already in row
            if digit in dupes: 
                return True
            # if digit is not in row, add to set
            else:
                dupes.add(digit)
                return False
