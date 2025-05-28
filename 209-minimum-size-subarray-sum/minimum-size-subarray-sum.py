class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        result = n+1
        left,right = 0,0
        sums = [0 for _ in range(n+1)]   #sums[i] = sum of (num[0],...,nums[i-1]) , i>=1
        for i in range(1,n+1):
            sums[i] = sums[i-1] + nums[i-1]
            if right == 0 and sums[i] >= target : right = i

        #print('sums:',sums,',left:',left,',right:',right)

        while right<n+1:
            while sums[right]-sums[left]>=target:
                result = min(result,right-left)
                left+=1
            right += 1
        
        return result if result!=n+1 else 0
        