# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def symmtric(left, right):
            if (left is None and right is not None) or (left is not None and right is None) : return False
            if left is None and right is None : return True
            if left.val != right.val : return False
            return symmtric(left.left,right.right) and symmtric(left.right,right.left)

        if not root : return True
        return symmtric(root.left,root.right)

        def foo(node):
            if (node.left is None and node.right is not None) or (node.left is not None and node.right is None):
                return False
            if node.left is None and node.right is None : 
                return True
            return foo(node.left) == foo(node.right)
        
        return foo(root)
        