class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = Counter()
        good_pairs = 0
        for i,num in enumerate(nums):
            diff = num - i
            good_pairs = good_pairs + cnt[diff]
            cnt[diff] += 1
        
        return (n-1)*2//2 - good_pairs 