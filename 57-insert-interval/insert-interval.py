class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        startIndex,endIndex = -1,-1   # 插入的区间，左右边分别落在哪个区间。如果-1表示不落在任何一个区间。但是没落在区间是啥意思？可能是任意的2个区间的中间。这可不好玩。
        # 所以这个方法不好。
        for i in range(len(intervals)): 
            interval = intervals[i]
            if interval[0]<=newInterval[0] and interval[1]>=newInterval[0]:
                startIndex = i
            if interval[0]<=newInterval[1] and interval[1]>=newInterval[1]:
                endIndex = i
        
        if startIndex>0 and endIndex < 0 :
            pass
        
        #还得用下面这个笨方法
        result = []
        n = len(intervals)
        index = 0

        while index<n and intervals[index][1]<newInterval[0]:
            result.append(intervals[index])
            index += 1

        while index<n and intervals[index][0]<=newInterval[1]:
            newInterval[0] = min(intervals[index][0],newInterval[0])
            newInterval[1] = max(intervals[index][1],newInterval[1])
            index += 1
        result.append(newInterval)

        while index<n:
            result.append(intervals[index])
            index += 1

        return result
