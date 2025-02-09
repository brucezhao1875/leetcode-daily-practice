class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = Counter()
        result = (n-1)*n//2
        for i,num in enumerate(nums):
            result -= cnt[num-i]
            cnt[num-i] += 1
        return result