class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        使用分治法求最大子数组和
        时间复杂度: O(n log n)
        空间复杂度: O(log n) - 递归栈空间
        """
        def divideConquer(nums, left, right):  # 去掉了 self 参数
            # 基础情况：只有一个元素
            if left == right:
                return nums[left]
            
            # 找到中点
            mid = (left + right) // 2
            
            # 递归求解左半部分的最大子数组和
            left_max = divideConquer(nums, left, mid)  # 递归调用不需要 self
            
            # 递归求解右半部分的最大子数组和
            right_max = divideConquer(nums, mid + 1, right)  # 递归调用不需要 self
            
            # 求解跨越中点的最大子数组和
            # 从中点向左扫描
            left_sum = float('-inf')
            current_sum = 0
            for i in range(mid, left - 1, -1):
                current_sum += nums[i]
                left_sum = max(left_sum, current_sum)
            
            # 从中点+1向右扫描
            right_sum = float('-inf')
            current_sum = 0
            for i in range(mid + 1, right + 1):
                current_sum += nums[i]
                right_sum = max(right_sum, current_sum)
            
            # 跨越中点的最大和
            cross_max = left_sum + right_sum
            
            # 返回三种情况的最大值
            return max(left_max, right_max, cross_max)

        return divideConquer(nums, 0, len(nums) - 1)
