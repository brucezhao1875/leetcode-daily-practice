class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices : return 0
        n = len(prices)
        #dp[i][2][2] 含义：
        #dp[i][0][0] :第i天闭市时，没有交易，不持有股票时的最大收益
        #dp[i][0][1] :第i天闭市时，没有交易，持有股票时的最大收益
        #dp[i][1][0] :第i天闭市时，最多1次交易，不持有股票时的最大收益
        #dp[i][1][1] :第i天闭市时，最多1次交易，持有股票时的最大收益
        dp = [ [[0,0],[0,0]] for _ in range(n)]
        dp[0][1][1] = -prices[0]
        for i in range(1,n):
            dp[i][1][0] = max( dp[i-1][1][0], dp[i-1][1][1]+prices[i] )
            dp[i][1][1] = max( dp[i-1][0][0] - prices[i], dp[i-1][1][1] )
        return dp[n-1][1][0]