class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        path = []
        def bt(nums, target, path, start):
            if target < 0 :
                return
            if target == 0 :
                result.append(path[:])
            for i in range(start,len(nums)):
                path.append(nums[i])
                bt(nums, target - nums[i], path, i)
                path.pop()
        
        bt(candidates, target, path, 0)
        return result

