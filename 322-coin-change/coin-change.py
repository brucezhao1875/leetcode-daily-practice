class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = amount + 1
        dp = [inf for _ in range(n)]
        dp[0] = 0
        for i in range(n):
            for coin in coins:
                if i >= coin :
                    dp[i] = min(dp[i],dp[i-coin]+1)

        return dp[n-1] if dp[n-1]!=inf else -1