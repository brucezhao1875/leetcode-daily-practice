# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
Method 1: I'm forgetting all standard solutions and deriving from scratch. I'll assume nodes can conveniently find their ancestor nodes.

Therefore, I need to first inject a property into TreeNode: a father node. How to do this: Python objects don't have great encapsulation, so I'll inject directly.
Now, I can efficiently implement a method to determine if two nodes have an ancestor relationship:
pythonwhile x.father is not None and x.father != y: 
    x = x.father
if x.father == y: 
    return True
Why this method needs to use father: because if searching downward from a high-level node, it means traversing all descendant nodes; but using the father node, we only need to traverse the path from x to root.
The current logic can be:
pythonwhile True:
    if r.left is ancestor of p and r.left is ancestor of q: r = r.left
    if r.right is ancestor of p and r.right is ancestor of q: r = r.right
    if r.left is ancestor of p and r.right is ancestor of q: return r
    if r.right is ancestor of p and r.left is ancestor of q: return r

Complexity Analysis:

isAncestor complexity: O(log n)
Overall framework complexity: O(log n)
Therefore, total complexity: O((log n)²)

For nodes on the scale of 10⁵, complexity is roughly 10⁴, which is completely fine.


Method 2：LCA has one mature solution that does not require injecting a father Node .

NOTICE that this is a binary search tree, which meeans the val of node is already in order. so we can judge how to travel through the tree by comparing p.val, q.val and root.val

'''
class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.lowestCommonAncestor2(root,p,q)


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



    def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
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
    
    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        x = root
        
        while True:
            if x.val == p.val or x.val == q.val : 
                return x
            if p.val < x.val and q.val < x.val :
                x = x.left
                continue
            if p.val > x.val and q.val > x.val:
                x = x.right
                continue
            if (p.val < x.val < q.val) or  (q.val < x.val < p.val):
                return x
                
        return x