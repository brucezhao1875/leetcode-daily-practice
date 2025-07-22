class Solution:

    '''
    分两步：step 1 ：找出转折点（如果存在）； 
          step 2 ：根据pivot分段做二分查找
    '''
    def search(self, nums: List[int], target: int) -> int:
        
        def find_rotated_pivot(nums) -> int:
            left, right = 0, len(nums) - 1
            if nums[left] < nums[right]:  # 已经有序，无旋转
                return 0
            while left < right:
                mid = (left + right) // 2
                if nums[mid] > nums[right]:  # pivot在右边
                    left = mid + 1
                else:  # pivot在左边或mid
                    right = mid
            return left  # 最小值索引（即pivot）

        def binary_search(nums, left, right, target):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        if not nums:
            return -1

        pivot = find_rotated_pivot(nums)
        n = len(nums)

        # 判断在哪一段
        if nums[pivot] <= target <= nums[n - 1]:
            return binary_search(nums, pivot, n - 1, target)
        else:
            return binary_search(nums, 0, pivot - 1, target)