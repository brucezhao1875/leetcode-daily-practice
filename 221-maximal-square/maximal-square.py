class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m,n = len(matrix),len(matrix[0])
        dp = [ [ 0 for _ in range(n) ] for _ in range(m) ]
        for i in range(m):
            dp[i][0] = 1 if matrix[i][0] == '1' else 0
        for j in range(n):
            dp[0][j] = 1 if matrix[0][j] == '1' else 0
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1]) + 1
        
        t = max( [ max(dp[row]) for row in range(m) ] )
        
        return t**2