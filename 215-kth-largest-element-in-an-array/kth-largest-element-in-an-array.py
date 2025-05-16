class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_select(nums,k):
            smaller,same,larger = [],[],[]
            pivot = nums[0]
            for x in nums:
                if x < pivot : smaller.append(x)
                elif x == pivot : same.append(x)
                else : larger.append(x)
            if len(larger) >= k :
                return quick_select(larger,k)
            elif len(larger) + len(same) >= k:
                return pivot
            else :
                 return quick_select(smaller,k-len(larger)-len(same))
        return quick_select(nums,k)

    def findKthLargest2(self, nums: List[int], k: int) -> int:
        nums.sort(key=lambda x : -x)
        return nums[k-1]