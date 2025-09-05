class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        #这题的陷阱是：s1/s2貌似被拆分成不同子串。实际上只需要逐个字符考虑，因为相邻字符连起来即为子串
        m,n = len(s1) , len(s2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        
        if m+n != len(s3):
            return 0


        dp[0][0] = 1
        
        for i in range(1,m+1) :
            if s1[i-1] == s3[i-1] :
                dp[i][0] = 1
            else:
                break
        
        for j in range(1,n+1):
            if s2[j-1] == s3[j-1]:
                dp[0][j] = 1
            else:
                break
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                if dp[i-1][j]==1 and s1[i-1]==s3[i+j-1] or dp[i][j-1]==1 and s2[j-1]==s3[i+j-1]:
                    dp[i][j] = 1
        
        return dp[m][n]