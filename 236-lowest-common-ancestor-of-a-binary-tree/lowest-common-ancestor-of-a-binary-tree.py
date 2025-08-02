# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None or root==p or root==q : return root
        x = self.lowestCommonAncestor(root.left,p,q)
        y = self.lowestCommonAncestor(root.right,p,q)
        if x is None and y is not None : 
            return y
        elif x is not None and y is None:
            return x
        elif x is not None and y is not None:
            return root
        else:
            return None
