class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        rows = [1 for _ in range(m)]
        cols = [1 for _ in range(n)]
        for i in range(m):
            for j in range(n):
                if not matrix[i][j]:
                    rows[i] = 0
                    cols[j] = 0
        for i in range(m):
            for j in range(n):
                if not rows[i] or not cols[j]:
                    matrix[i][j] = 0
