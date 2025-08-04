class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def gcd(a,b):
            return a if b==0 else gcd(b,a%b)
        
        points.sort()
        n = len(points)
        result = 1
        for i in range(n):
            mapping = {}
            cnt = 0
            x1,y1 = points[i]
            for j in range(i+1,n):
                x2,y2 = points[j]
                a,b = x2-x1,y2-y1
                k = gcd(a,b)
                a,b = a//k,b//k
                key = str(a)+'_'+str(b)
                mapping[key] = mapping.get(key,0)+1
                cnt = max(cnt,mapping[key])
            result = max(result,cnt+1)
        return result        