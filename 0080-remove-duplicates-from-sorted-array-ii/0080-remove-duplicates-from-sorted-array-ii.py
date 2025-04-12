class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <=2 : return n

        p = 1
        for i in range(2,n):
            if nums[i] != nums[p-1]:
                p += 1
                nums[p] = nums[i]
        return p+1
