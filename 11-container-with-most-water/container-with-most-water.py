class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left,right = 0,n-1
        result = 0
        while left < right:
            result = max(result, (right-left)*min(height[left],height[right]))
            if height[left]<height[right]:
                left += 1
            else:
                right -= 1
        return result