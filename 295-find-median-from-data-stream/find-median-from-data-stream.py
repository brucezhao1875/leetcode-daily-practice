class MedianFinder:
    '''
    def __init__(self):
        # 只用一个堆
        self._heap = []

    def addNum(self, num: int) -> None:
        # 步骤 1：先加入最大堆（取负数）
        heapq.heappush(self._heap, num)
    def findMedian(self) -> float:
        n = len(self._heap)
        print(self._heap,"###",n)
        return  ( self._heap[n // 2] + self._heap[n // 2 - 1] ) / 2 if  n & 1 == 0  else self._heap[ n // 2]
    '''
    def __init__(self):
        # max_heap 模拟最大堆，存放较小一半（取负数）
        self.max_heap = []
        # min_heap 是最小堆，存放较大一半
        self.min_heap = []

    def addNum(self, num: int) -> None:
        # 步骤 1：先加入最大堆（取负数）
        heapq.heappush(self.max_heap, -num)
        
        # 步骤 2：把最大堆堆顶元素移到最小堆
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        
        # 步骤 3：如果最小堆比最大堆大了，则再移动一个回来
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else:
            # 两堆元素数量相等，取两堆堆顶均值
            return (-self.max_heap[0] + self.min_heap[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()