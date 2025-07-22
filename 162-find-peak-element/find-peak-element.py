class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right :
            mid = (left + right) // 2
            if nums[mid] < nums[mid+1] :
                left = mid + 1
            elif nums[mid] > nums[mid+1]:
                right = mid
            else:
                return -1  # impossible condition
        return right