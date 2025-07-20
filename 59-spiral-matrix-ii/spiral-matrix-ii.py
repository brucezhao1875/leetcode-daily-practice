class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        stats = [[0 for _ in range(n)] for _ in range(n)]
        deltas = [(0,1),(1,0),(0,-1),(-1,0)]
        direction = 0
        x,y = 0,0
        for i in range(n*n):
            matrix[x][y] = i + 1
            stats[x][y] = 1
            delta = deltas[direction]
            x_,y_ = x + delta[0] , y + delta[1]
            if not ( x_ >=0 and x_ <= n-1 and y_>=0 and y_<=n-1 and stats[x_][y_]==0 ) :
                direction = (direction + 1) % 4
                delta = deltas[direction]
                x_,y_ = x + delta[0] , y + delta[1]
            x,y = x_,y_

        return matrix