class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = Counter()
        result = 0
        for num in nums:
            result += cnt[num]
            cnt[num] += 1
        return result