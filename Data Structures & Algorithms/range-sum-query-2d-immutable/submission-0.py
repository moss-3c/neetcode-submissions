class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = []
        rows = len(matrix)
        cols = len(matrix[0])
        self.prefix = [[0] * (cols + 1) for _ in range(rows + 1)]

        for r in range(rows):
            rowPrefix = 0
            for c in range(cols):
                rowPrefix += matrix[r][c]
                sumAbove = self.prefix[r][c + 1]
                self.prefix[r + 1][c + 1] = rowPrefix + sumAbove

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.prefix[row2 + 1][col2 + 1] # bottom right
            - self.prefix[row2 + 1][col1]  # left
            - self.prefix[row1][col2 + 1]  # above
            + self.prefix[row1][col1]     # upper left
        )


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)