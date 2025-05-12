# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #deque的方法,这个更直观更顺手
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root : return 0
        q = deque()
        q.append(root)
        level = 0
        while q:
            n = len(q)
            for i in range(n):
                x = q.popleft()
                if x.left : q.append(x.left)
                if x.right : q.append(x.right)
            level += 1
        return level
    
    def maxDepth2(self, root: Optional[TreeNode]) -> int:
        def transverse(n):
            if not n : return 0
            return max(transverse(n.left),transverse(n.right)) + 1

        return transverse(root)