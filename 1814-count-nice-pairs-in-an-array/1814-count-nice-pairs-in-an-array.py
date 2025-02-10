class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(num):
            x = list(str(num))
            x.reverse()
            while x[0] == 0 :
                x = x[1:]
            return int(''.join(x))
        
        n = len(nums)
        
        diff_nums = [ (num - rev(num)) for num in nums ]
        
        cnt = Counter()
        result = 0
        for x in diff_nums:
            result = (result + cnt[x] ) % (10**9 + 7) 
            cnt[x] += 1

        return result

        