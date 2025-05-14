class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid), len(grid[0])
        def dfs(i,j):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j] == '0' : return
            grid[i][j] = '0'
            for di,dj in ((0,1),(0,-1),(1,0),(-1,0)) :
                dfs(i+di,j+dj)
        
        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' : 
                    result += 1
                    dfs(i,j)
        return result