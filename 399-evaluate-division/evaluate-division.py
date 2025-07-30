'''
1、这个类型的题目，可以用并查集的方式来做
2、并查集的核心是：要在merge和is_connected()之间做权衡
  -- 如果每个节点的父节点都指向了祖先节点（即：做了路径压缩），那么is_connected(x,y) 和 find() 很高效是O(1)，但是merge就不太高效

3、回到此case中，它的计算量太小了。只要有个实现的方式就可以。
'''
class UnionFind:
    def __init__(self):
        self.parents = {}
        self.values = {}


    def find(self,x):
        node = x
        base = 1
        while self.parents[node] is not None:
            node = self.parents[node]
            base *= self.values[node]
        
        root = node #这个集合的根节点

        # 合并路径啊兄弟们。这里就这么做了，实际上在本题这个case下，没有效率上的必要。
        while x != root:
            original_parent = self.parents[x]
            self.values[x] *= base
            base /= self.values[original_parent]
            self.parents[x] = root
            x = original_parent
        
        return root
        
    def merge(self,x,y,val):
        root_x,root_y = self.find(x),self.find(y)
        if root_x != root_y :
            self.parents[root_x] = root_y
            self.values[root_x] = self.values[y] * val / self.values[x]

    def is_connected(self,x,y):
        return x in self.values and y in self.values and self.find(x) == self.find(y)

    def add(self,x):
        if x not in self.parents:
            self.parents[x] = None
            self.values[x] = 1.0

class Solution:
     def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        uf = UnionFind()
        for (a,b),val in zip(equations,values):
            uf.add(a)
            uf.add(b)
            uf.merge(a,b,val)
        result = [-1.0] * len(queries)
        for i,(a,b) in enumerate(queries):
            if uf.is_connected(a,b):
                result[i] = uf.values[a] / uf.values[b]
        return result           

