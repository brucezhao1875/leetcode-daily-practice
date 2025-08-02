# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
方法一：我把标准解法统统忘掉，现在从头开始推演。我要假设节点能够方便地找到它的祖先节点，
1、因此我需要首先给TreeNode注入一个属性：father节点。那这个怎么做：python对象的封闭性没有那么好，我直接注入。
2、现在，我可以高效地实现一个方法：判断两个节点是否有ancestor关系： while x.father is not None and x.father!=y : x = x.father ; if x.father == y : return true
    为什么这个方法需要用到father：因为如果是从高层节点往下找，那么意味着需要遍历所有后代节点；而采用father节点，则只需要遍历从x到root的这条路径。
3、现在的逻辑可以是：
    while true:
        if r.left is ancestor of p and r.left is ancestor of q :  r = r.left
        if r.right is ancestor of p and r.right is ancestor of q : r = r.right
        if r.left is ancestor of p and r.right is ancestor of q : return r
        if r.right is ancestor of p and r.left is ancestor of q : return r

4、复杂度分析
    isAncestor的复杂度：O(logn)
    整体框架的复杂度：O(logn)
    因此整体复杂度为：O( (logn)^2 ). 对于nodes为( 10^5 )的量级，复杂度大致为（ 10000 ），完全没有问题。

方法二：LCA有一个成熟的解法，是不需要注入father节点的。

'''
class Solution:
    def updateFatherRef(self, father,node):
        if node is None : return
        node.father = father
        self.updateFatherRef(node,node.left)
        self.updateFatherRef(node,node.right) 

    def isAncestor(self,descendant,ancestor):
        if descendant is None or ancestor is None : return False
        x = descendant
        while x.father is not None:
            if x == ancestor :
                return True
            x = x.father
        return False

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #第一步，先把father属性注入
        self.updateFatherRef(None,root)
        r = root
        while True:
            if r == p or r == q : return r
            if (self.isAncestor(p,r.left) and self.isAncestor(q,r.right)) or  (self.isAncestor(q,r.left) and self.isAncestor(p,r.right)) : return r
            if (self.isAncestor(p,r.left) and self.isAncestor(q,r.left)):
                r = r.left
                continue
            if (self.isAncestor(p,r.right) and self.isAncestor(q,r.right)):
                r = r.right
                continue
        return r