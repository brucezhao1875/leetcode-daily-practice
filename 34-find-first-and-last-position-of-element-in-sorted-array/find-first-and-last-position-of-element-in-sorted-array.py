class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(nums,target,lower_flag):
            result = -1
            n = len(nums)
            left,right = 0,n-1
            while left<=right:
                mid = (left+right)//2
                if nums[mid] < target : left = mid + 1
                elif nums[mid] > target : right = mid - 1
                else:
                    result = mid
                    if lower_flag:
                        right = mid - 1
                    else:
                        left = mid + 1
            return result
        leftIndex = binarySearch(nums,target,True)
        rightIndex = binarySearch(nums,target,False)
        return [leftIndex,rightIndex]