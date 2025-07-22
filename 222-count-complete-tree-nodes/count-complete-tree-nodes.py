# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
1、关于calculate height： 树的操作也可以用递归方法，最简单。但是有个问题：为什么类似"爬楼梯"的题目要用dp?
    - 重复计算的复杂度基础都是 O(a^n) ， 不同的是：a==1 时，退化为O(n) 它就不是事； 爬楼梯时a==2 ，就变成O(2^n)
    - 比如tree的操作，如果你是求root的某个属性，那么递归的话就是O(n)，每个节点遍历一次；
        但是如果你要对所有节点求属性，又是从root往下的计算的话，那么计算次数就是n+(n-1)+(n-2)+... = O(n^2),貌似问题也不大
        但是如果爬楼梯，那就是O(2^n)
        为什么有这个不同？其实它们都满足一个公式：O(a^n)，只不过tree里边那个情况它a=1，而爬楼梯里边

    -- tree还有个好处嘛，就是height为O(logn)，这个属性牛逼。所以有时候吧，即使你遇到爬楼梯一样的O(2^n)的重复计算，它也不会出问题，因为这里边的n变成了height(tree) == log n ,那就都不是事了。
    比如我在leetcode.cn里边写的一个算法，实际它也涉及了重复计算，就是这种情况。

2、在这么一个easy题目里边这么纠缠，有意思吗？当然有意思：dp、递归内部的机制；tree的O(logn)特性。不然我们每次就只能稀里糊涂地试。

3、最后再说这个破题：它就是要定位到最后一个left is not None but right is None 的节点，那就是最后一个节点的父节点。
    找到这个节点之后，如果你知道它的路径，那就可以完成计算。以0-left/1-right为例，如果final-parent 的路径为：1，那就能计算了对吧。可以用2^n 之类的算出来。
    不过那都不是重点了，事情分析到这个地步，就看答案呗。
    如下2个，一个是O(n) ，一个是O(logn)

'''
class Solution:
    def countNodes2(self, root: Optional[TreeNode]) -> int:
        if not root : return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        level = 0
        node = root.left
        while node:  # 这里获得层数
            level += 1
            node = node.left
        l = 1<<level  # 左界
        r = (l<<1)-1  # 右界

        while l < r:
            mid = int((r+l+1)/2)  # 中位
            node = root
            path = 1<<(level-1)  # 取mid号数的后几位的模板
            while node and path > 0:
                if mid & path: node = node.right
                else: node = node.left
                path >>= 1  # 一层查完，查下一层
            if node: l = mid  # 存在left位置变化
            else: r = mid-1  # 不存在right位置变化
        return r  # 年轻人耗子尾汁


        