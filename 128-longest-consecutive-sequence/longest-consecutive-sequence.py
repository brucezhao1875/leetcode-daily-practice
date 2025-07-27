class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        result = 0
        #print(counter.keys())
        keys = sorted(counter.keys())
        for num in keys:
            if counter[num-1] == 0:
                seq_len = 1
                while counter[num+1]:
                    seq_len += 1
                    num += 1
                result = max(result,seq_len)
        return result
