class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = list(range(len(nums)))
        indices.sort(key = lambda x : nums[x])
        left,right = 0,len(nums)-1
        while left<right:
            sum = nums[indices[left]] + nums[indices[right]]
            if sum == target:
                return [indices[left],indices[right]]
            elif sum < target:
                left += 1
            else:
                right -= 1

