class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        bad_pairs = 0
        diff_count = {}
        for pos in range(n):
            diff = pos - nums[pos]

            #count of previous positions with same difference
            good_pairs_count = diff_count.get(diff,0)

            #total possible pairs minus good pairs = bad pairs
            bad_pairs += pos - good_pairs_count

            #update count of positions with this difference
            diff_count[diff] = good_pairs_count + 1
        
        return bad_pairs