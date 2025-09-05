class Solution:
    def mySqrt(self, x: int) -> int:
        left,right = 0,x
        while left <= right:
            mid = (left+right) // 2
            if mid**2 <=x and (mid+1)**2 >x :
                return mid
            elif mid**2 > x :
                right = mid - 1
            else:
                left = mid + 1