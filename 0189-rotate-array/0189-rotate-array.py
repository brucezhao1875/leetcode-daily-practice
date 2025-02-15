class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def swap(nums,i,j):
            while i<j:
                t = nums[i]
                nums[i] = nums[j]
                nums[j] = t
                i += 1
                j -= 1

        n = len(nums)
        k = k % n
        swap(nums,0,n-1)
        swap(nums,0,k-1)
        swap(nums,k,n-1)
        