class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = list(range(len(nums)))
        indices.sort(key=lambda x: nums[x])
        left,right = 0,len(nums)-1
        while left<right:
            t = nums[indices[left]] + nums[indices[right]]
            if t < target:
                left += 1
            elif t > target:
                right -= 1
            else:
                return [indices[left],indices[right]]
        return [-1,-1]