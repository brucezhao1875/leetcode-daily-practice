class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0 
        right = n-1
        while left <= right :
            mid = (left + right) // 2
            x = nums[mid]
            if x < target :
                left = mid + 1
            elif x > target :
                right = mid-1
            else:
                return mid 
        return left