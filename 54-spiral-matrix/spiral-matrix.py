class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        cnt = m*n
        result = [0 for _ in range(cnt)]

        direction = 0
        deltas = [(0,1), (1,0), (0,-1), (-1,0)] 
        stats = [[0 for _ in range(n)] for _ in range(m)]
        x = 0  # current row 
        y = 0  # current col    

        for i in range(cnt):
            result[i] = matrix[x][y]
            stats[x][y] = 1

            delta = deltas[direction]
            x_ = x + delta[0]
            y_ = y + delta[1]
            if not ( x_ <= m-1 and x_ >=0 and y_ <= n-1 and y_ >= 0 and stats[x_][y_] == 0 ) :
                direction = (direction + 1) % 4
                delta = deltas[direction]
                x_ = x + delta[0]
                y_ = y + delta[1]
            
            x,y = x_,y_
        
        return result