class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # dp[i] 表示和为 i 的排列数量
        dp = [0] * (target + 1)
        dp[0] = 1  # 和为0的排列数量为1（空排列）
        
        # 对于每个目标值
        for i in range(1, target + 1):
            # 尝试每个数字作为最后一个数
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]
        
        return dp[target]