# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def transverse(n):
            if not n : return 0
            return max(transverse(n.left),transverse(n.right)) + 1

        return transverse(root)