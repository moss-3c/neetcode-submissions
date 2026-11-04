class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find row
        row = 0
        l, r = 0, len(matrix) - 1
        while l <= r:
            row = (l + r) // 2

            if matrix[row][0] == target:
                return True
            elif matrix[row][0] < target:
                l = row + 1
            else:
                r = row - 1
        
        if matrix[row][0] > target: 
            row -= 1
        
        # row is now the row target must be in
        l, r = 0, len(matrix[row]) - 1
        m = 0
        while l <= r:
            m = (l + r) // 2

            if matrix[row][m] == target:
                return True
            elif matrix[row][m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return matrix[row][m] == target