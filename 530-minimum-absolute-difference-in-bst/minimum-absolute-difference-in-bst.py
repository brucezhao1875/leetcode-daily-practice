# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def transverse(node,nums):
            if node is None: return
            transverse(node.left,nums)
            nums.append(node.val)
            transverse(node.right,nums)
        
        nums = []
        transverse(root,nums)
        n = len(nums)
        result = 2**31
        for i in range(n-1):
            result = min(result,nums[i+1]-nums[i])
        return result