class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        result = []
        path = []
        def bt(nums, target, path, start):
            if target < 0 :
                return
            if target == 0 :
                result.append(path[:])
                return
            for i in range(start, n):
                path.append(nums[i])
                bt(nums, target - nums[i], path, i)
                path.pop()
        
        bt(candidates, target, path, 0)
        return result


