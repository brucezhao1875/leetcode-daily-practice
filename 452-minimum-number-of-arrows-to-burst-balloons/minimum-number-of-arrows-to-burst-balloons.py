class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points : 
            return 0

        n = len(points)
        points.sort(key = lambda x: x[1])
        
        pos = points[0][1]
        result = 1
        
        for x in points:
            if x[0] > pos :
                result += 1
                pos = x[1]

        return result
