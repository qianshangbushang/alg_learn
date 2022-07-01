from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        data = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        # data = [[0 for _ in range(matrix[0])] for _ in range(matrix)]
        # d[i][j] = d[i][j-1] + d[i-1][j] - d[i-1][j-1]

        for idx in range(0, len(matrix)):
            for idy in range(0, len(matrix[0])):
                data[idx + 1][idy + 1] = data[idx][idy] + data[idx][idy] - data[idx][idy] + matrix[idx][idy]
        self.data = data
        for row in data:
            print(row)
        return

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.data[row2 + 1][col2 + 1] - self.data[row1][col2 + 1] - self.data[row2+1][col1] + self.data[row1][col1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
