"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    #
    # 注意random的值是node的下标。那就好办：1、先遍历出节点数n；2、初始化一个状态数组：0：初始状态，1：第一状态；2：完全就绪状态。
    # 也可以这样：构建一个[]，先把队列构建出来，把各个元素放到[]中；然后第二轮再修改random
    # 不对,虽然构造函数中random是下标，但实际上指向的是引用。因此上面说的不对。
    #
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dict = {}
        p = head
        while p :
            dict[p] = Node(p.val)
            p = p.next
        p = head
        while p :
            x = dict[p]
            x.next = dict.get(p.next)
            x.random = dict.get(p.random)
            p = p.next
        return dict.get(head)
        