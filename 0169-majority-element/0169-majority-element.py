class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        for num in nums:
            if not count:
                candidate = num
            count += ( 1 if num == candidate else -1 )
        
        return candidate