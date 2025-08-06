class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        def dfs(board,m,n,i,j,k,word):
            if k >= len(word): return True
            if not 0<=i<m or not 0<=j<n or not board[i][j] == word[k] :  return False
            
            board[i][j] = '#'
            deltas = [[-1,0],[0,1],[1,0],[0,-1]]
            for delta in deltas:
                next_i = i + delta[0]
                next_j = j + delta[1]
                if dfs(board,m,n,next_i,next_j,k+1,word) :
                    return True
            board[i][j] = word[k]
            return False

        for i in range(m):
            for j in range(n):
                if dfs(board,m,n,i,j,0,word):
                    return True
        return False