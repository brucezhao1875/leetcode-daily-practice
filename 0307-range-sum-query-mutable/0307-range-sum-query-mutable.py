class NumArray:

    '''

    这题奇技淫巧的，令人厌恶。但是既然要搞，就把它搞定。
    
    lowbit(x) = x & -x
    代表：二进制低位第一次出现1的数，
    假设bin(x)的低位为:1后面n个0,like:1000...000 那么-x的补码表示 0后面n个1，再+1，自然也是：1后面n个0
    那么x&-x的结果是：二进制低位第一次出现1时，对应的那个数字。就是：1后面n个0。

    有了lowbit(x),再看怎么使用。体会一下如下2个逻辑：
    1、树状数组中的节点i，其父节点（唯一）是i+lowbit(i)
    2、树状数组中的节点i，i-lowbit(i)是其子节点。 -- 它等价于上句话。

    为什么选择i+lowbit(i)作为父节点？看一下例子，有什么规律：
    例如i=13=8+4+1，它的父节点是13+1=14，
    i=5=4+1，它的节点是5+1=6
    i=6=4+2，父节点是4+2+2=8
    i=4，父节点是8

    什么道理？构造一个数组看一下：
    1 - 2
    2，3 - 4
    4，6，7 - 8
    5 - 6
    8 - 16
    9 - 10
    10 - 12
    11 - 12 
    13 - 14

    卧槽，看出来什么规律了没


    '''

    # __slots__ = 'nums','tree'

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.nums = [0 for _ in range(n)]
        self.tree = [0 for _ in range(n+1)]
        for i,x in enumerate(nums):
            self.update(i,x)

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.nums[index] = val
        i = index + 1
        while i < len(self.tree):
            self.tree[i] += delta
            i = i + (i&-i)
    
    def prefixSum(self,i:int):
        s = 0
        while i:
            s += self.tree[i]
            i = i - (i&-i)
        return s

    def sumRange(self, left: int, right: int) -> int:
        return self.prefixSum(right+1) - self.prefixSum(left)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
