class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left,right = 0,n-1
        found = False
        while left < right and not found:
            x = numbers[left] + numbers[right]
            if x == target:
                found = True
                return [left+1,right+1]
            elif x > target:
                right = right -1
            else:
                left = left + 1
        return []