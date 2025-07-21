# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = -inf
        def dfs(node):   #对上级的贡献度
            if not node : return 0
            l_val = dfs(node.left)
            r_val = dfs(node.right)

            nonlocal result
            # 路径可以被分解为"不重叠可并集":顶点为node的路径的和。顶点表示最高点（拐弯处），node∈全部node的集合
            # 由于遍历所有node，因此形成全覆盖。
            result = max(result,l_val + r_val + node.val)  # 在node处拐弯，包含node点的path值。 

            return max(0,max(l_val,r_val)+node.val)

        dfs(root)
        return result