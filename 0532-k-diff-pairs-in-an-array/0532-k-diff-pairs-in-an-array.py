class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        visited = set()
        result = set()
        
        for num in nums:
            if num-k in visited:
                result.add(num-k)
            if num+k in visited:
                result.add(num)
            visited.add(num)
        
        return len(result)