class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # search col for right row
        l, r = 0, len(matrix) - 1 # num rows
        m, n = None, len(matrix[0]) - 1 # n=last idx of row
        while l <= r: # l to r incl = possible rows
            m = l + (r - l) // 2
            if target < matrix[m][0]: # target is in earlier row
                r = m - 1
            elif target > matrix[m][n]: # target in later row
                l = m + 1
            else:
                break
        # search row
        # m=row to search
        l, r = 0, n
        while l <= r: 
            mid = l + (r - l) // 2
            if matrix[m][mid] < target: # eliminate left half
                l = mid + 1
            elif matrix[m][mid] > target: # elim right half
                r = mid - 1
            else:
                return True
        
        return False
