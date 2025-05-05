# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result = []
        q = [root]
        while q :
            v = 0
            p = []
            for x in q:
                v += x.val
                if x.left : p.append(x.left)
                if x.right : p.append(x.right)
            result.append(v/len(q))
            q = p
        return result
        