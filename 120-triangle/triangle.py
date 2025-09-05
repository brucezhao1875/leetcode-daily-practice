class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dps = [ [ 0 for _ in range(row+1)] for row in range(n)]
        dps[0] = triangle[0]
        
        for row in range(1,n):
            dps[row][0] = dps[row-1][0] + triangle[row][0]
            for col  in range(1,row):
                dps[row][col] = min(dps[row-1][col-1],dps[row-1][col]) + triangle[row][col]
            dps[row][row] = dps[row-1][row-1] + triangle[row][row]
        
        return min(dps[n-1])