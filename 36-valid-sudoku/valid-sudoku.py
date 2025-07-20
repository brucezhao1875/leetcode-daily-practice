class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def isvalidRows(board: List[List[str]]) -> bool:
            for i in range(9):
                stats = set()
                for j in range(9):
                    if board[i][j] != '.' and board[i][j] in stats: return False
                    stats.add(board[i][j])
            return True
        
        def isvalidCols(board: List[List[str]]) -> bool:
            for j in range(9):
                stats = set()
                for i in range(9):
                    if board[i][j] != '.' and board[i][j] in stats: return False
                    stats.add(board[i][j])
            return True

        def isvalidSubBoxes(board: List[List[str]]) -> bool:
            for i in range(3):
                for j in range(3):
                    stats = set()
                    for x in range(3):
                        for y in range(3):
                            c = board[3*i+x][3*j+y]
                            if c != '.' and c in stats: return False
                            stats.add(c)
            return True
        
        return isvalidRows(board) and isvalidCols(board) and isvalidSubBoxes(board)
        
        