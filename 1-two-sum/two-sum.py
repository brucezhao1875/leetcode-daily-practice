class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 创建一个数组，保存原始索引
        indices = list(range(len(nums)))
        # 根据 nums 的值排序 indices
        indices.sort(key=lambda i: nums[i])

        low = 0
        high = len(nums) - 1

        while low < high:
            sum_val = nums[indices[low]] + nums[indices[high]]
            if sum_val == target:
                return [indices[low], indices[high]]
            elif sum_val < target:
                low += 1
            else:
                high -= 1
