class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dict_hash = {k:k for k in wordDict}
        n = len(s)
        dp = [ 0 for _ in range(n+1) ]
        dp[0] = 1

        for i in range(1,n+1):
            for j in range(i):
                if dp[j] and s[j:i] in dict_hash:
                    dp[i] = 1
                    break

        return True if dp[n] == 1 else False 