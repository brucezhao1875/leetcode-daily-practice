# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None : return []
        q = [root]
        result = []
        zigzag_flag = True
        while len(q)>0:
            level = []
            q_2 = []
            for x in q:
                level.append(x.val)
                if x.left is not None : q_2.append(x.left)
                if x.right is not None : q_2.append(x.right)
            
            result.append(level if zigzag_flag else level[::-1])
            zigzag_flag = not zigzag_flag
            q = q_2
        return result