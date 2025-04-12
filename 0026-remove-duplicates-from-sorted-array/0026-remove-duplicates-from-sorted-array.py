class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        p = 0
        for i in range(1,n):
            if nums[p] != nums[i]:
                p += 1
                nums[p] = nums[i]                
        return p+1

        