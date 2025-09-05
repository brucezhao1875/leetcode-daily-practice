class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        projects = sorted(zip(profits,capital),key = lambda x:x[1])
        heap = []
        idx = 0

        while k> 0 :
            while idx<n and projects[idx][1] <= w:
                heapq.heappush(heap,-projects[idx][0])
                idx += 1
            if heap:
                w -= heapq.heappop(heap)
            else:
                break
            k-=1

        return w
