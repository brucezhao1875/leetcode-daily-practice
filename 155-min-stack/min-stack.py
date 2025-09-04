class MinStack:

    #
    # 最有意思的地方是：1、要保存最小值的索引；2、为了保存最小值索引,只需要判断：当前最小索引=argmin(当前值,历史最小值)
    #

    def __init__(self):
        self.stack = []
        self.min_values = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_values) == 0 :
            self.min_values.append(val)
        else:
            self.min_values.append(min(self.min_values[-1],val))

    def pop(self) -> None:
        self.stack.pop()
        self.min_values.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_values[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()