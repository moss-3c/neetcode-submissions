class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # O(1) space
        dupes = {} # contains numbers the row/col/subgrid already has

        # check all rows are valid O(n^2)
        for i in range(9):
            for j in range(9):
                # checking single row
                digit = board[i][j]
                if self.digitAlreadyExists(dupes, digit):
                    return False
            # clear dupes after checking each row
            dupes = {}
        
        # check all cols are valid O(n^2)
        for i in range(9):
            # checking a single col
            for j in range(9):
                digit = board[j][i]
                if self.digitAlreadyExists(dupes, digit):
                    return False
            # clear dupes after checking each col
            dupes = {}

        # maybe can combine these two into 1 step and use 2 freq dict (col_dupes row_dupes)

        # check all subgrids are valid O(n^2)

        # loop through subgrids: index 0, 3, 6
        for row_offset in (range(0, 9, 3)):
            for col_offset in (range(0, 9, 3)):

                # check subgrid is valid
                for i in range(row_offset, row_offset + 3):
                    for j in range(col_offset, col_offset + 3):
                        digit = board[i][j]
                        if self.digitAlreadyExists(dupes, digit):
                            return False
                # clear dupes after checking each subgrid
                dupes = {}
        
        return True


    def digitAlreadyExists(self, dupes, digit: int) -> bool:
        # if cell is not blank
        if digit == '.':
            return False
        else:
            # if digit is already in row
            if dupes.get(digit) is not None: 
                return True
            # if digit is not in row, add to dict
            else:
                dupes[digit] = 1
                return False
