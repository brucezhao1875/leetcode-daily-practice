class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        p = 0
        for i in range(n):
            if nums[i] != val:
                nums[p] = nums[i]
                p += 1
        return p