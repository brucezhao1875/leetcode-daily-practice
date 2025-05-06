"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

# 要点：用到了多维的presum
class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        presum = [ [0 for _ in range(n+1)] for _ in range(n+1) ]
        for i in range(n):
            for j in range(n):
                presum[i+1][j+1] = presum[i+1][j] + presum[i][j+1] - presum[i][j] + grid[i][j]
        
        def getSum(r0:int, c0:int,r1:int,c1:int) -> int:
            return presum[r1][c1] - presum[r1][c0] - presum[r0][c1] + presum[r0][c0]
        
        def dfs(r0,c0,r1,c1) -> 'Node':
            total = getSum(r0,c0,r1,c1)
            if total == 0:
                return Node(False,True)
            if total == (r1-r0)*(c1-c0):
                return Node(True,True)
            return Node(
                True,
                False,
                dfs(r0,c0,(r0+r1)//2,(c0+c1)//2),
                dfs(r0,(c0+c1)//2,(r0+r1)//2,c1),
                dfs((r0+r1)//2,c0,r1,(c0+c1)//2),
                dfs((r0+r1)//2,(c0+c1)//2,r1,c1)
            )
        
        return dfs(0,0,n,n)