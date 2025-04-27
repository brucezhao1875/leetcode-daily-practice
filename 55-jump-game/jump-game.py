class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_reach = 0
        for i in range(n):
            #print (i,",",max_reach,"\n")
            if i > max_reach:
                return False
            max_reach = max(max_reach,i + nums[i])
            if max_reach >= n-1:
                return True
        return False