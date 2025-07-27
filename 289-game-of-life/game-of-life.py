class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m = len(board)
        n = len(board[0])
        deltas = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
        def cell_status(row,col):
            neighbors = 0
            for delta in deltas:
                if row+delta[0]>=0 and row+delta[0]<=m-1 and col+delta[1]>=0 and col+delta[1]<=n-1:
                    neighbors += board[row+delta[0]][col+delta[1]]
            
            status = board[row][col]
            result = status
            if status==1:
                if neighbors<=1: result = 0
                elif neighbors<=3: result = 1
                else: result = 0 
            else:
                if neighbors==3: result=1
            return result
        
        new_board = copy.deepcopy(board)
        for row in range(m):
            for col in range(n):
                new_board[row][col] = cell_status(row,col)
        
        for row in range(m):
            for col in range(n):
                board[row][col] = new_board[row][col]