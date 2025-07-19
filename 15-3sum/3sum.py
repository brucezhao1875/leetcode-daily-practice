class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        n = len(nums)
        for i in range(n-2):
            if nums[i] > 0 : break
            if i-1 >= 0 and nums[i] == nums[i-1] : continue
            j,k = i+1,n-1
            while j<k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                    while j<k and nums[j]==nums[j-1] : j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                    while j<k and nums[k] == nums[k+1] : k -= 1
                else:
                    result.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
                    while j<k and nums[j]==nums[j-1] : j+=1
                    while j<k and nums[k]==nums[k+1] : k-=1
        
        return result
