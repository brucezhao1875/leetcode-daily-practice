# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        #将节点转为单链表，按照先序遍历的顺序。返回：head、tail，指向单链表的头、尾
        def dfs(node: TreeNode):
            if not node: return
            head, tail = node, node
            if node.left is not None:
                left_head, left_tail = dfs(node.left)
                left_tail.right = node.right
                node.right = left_head
                node.left = None
                tail = left_tail
            if node.right is not None:
                right_head, right_tail = dfs(node.right)
                tail = right_tail
                node.right = right_head
            return head, tail
            
        dfs(root)