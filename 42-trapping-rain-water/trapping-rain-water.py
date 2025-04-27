class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftHeight = [0 for _ in range(n)]
        x = height[0]
        for i in range(n):
            leftHeight[i] = x
            x = max(x,height[i])
        rightHeight = [0 for _ in range(n)]
        x = height[n-1]
        for i in range(n-1,-1,-1):
            rightHeight[i] = x
            x = max(x,height[i])
        
        result = [ max(0, min(leftHeight[i],rightHeight[i]) - height[i]) for i in range(n) ]
        return sum(result)