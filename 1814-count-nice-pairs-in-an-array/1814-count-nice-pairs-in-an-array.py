class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(num):
            x = list(str(num))
            x.reverse()
            while x[0] == 0 :
                x = x[1:]
            return int(''.join(x))
        
        def rev2(num):
            result = 0
            while num:
                result = result * 10 + num % 10
                num = num //10
            return result

        def rev3(num):
            return int( str(num)[::-1] )

        
        diff_nums = [ (num - rev3(num)) for num in nums ]
        
        cnt = Counter()
        result = 0
        for x in diff_nums:
            result = (result + cnt[x] ) % (10**9 + 7) 
            cnt[x] += 1

        return result

        