class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        result = []

        def bt(nums, target, path, startIndex):
            if target < 0 :
                return
            if target == 0 :
                result.append(path[:])
            for i in range(startIndex, n):
                # 关键：跳过同一层的重复元素
                if i > startIndex and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                bt(nums, target - nums[i], path, i+1)
                path.pop()
        
        bt(candidates, target, [], 0)
        return result