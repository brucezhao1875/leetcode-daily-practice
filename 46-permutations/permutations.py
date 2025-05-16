class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def bfs(nums):
            result = []
            n = len(nums)
            if n == 0 : return [[]]
            for i in range(n):
                nums_copy = nums.copy()
                num = nums_copy.pop(i)
                items = bfs(nums_copy)
                for item in items:
                    result.append([num] + item)
            return result
        return bfs(nums)
    
    
    def permute2(self, nums: List[int]) -> List[List[int]]:

        def bfs(nums):
            result = []
            n = len(nums)
            if n == 0 :
                return [[]]
            for i in range(n):
                nums_copy = nums.copy()
                num = nums_copy.pop(i)
                items = bfs(nums_copy)
                for item in items:
                    result.append([num] + item)
            return result
        
        return bfs(nums)