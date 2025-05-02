class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        debug = 0
        n = len(intervals)
        result = []
        intervals.sort(key = lambda x:x[0])
        item = intervals[0]
        for i in range(1,n):
            interval = intervals[i]
            if interval[0] > item[1]:
                result.append(item)
                item = interval
            else:
                item[1] = max(interval[1],item[1])
        result.append(item)
        debug and print(result)
        return result