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
            if not node: 
                return

            if node.left is None and node.right is None:
                return node,node

            elif node.left is None and node.right is not None:
                right_head, right_tail = dfs(node.right)
                node.right = right_head
                return node,right_tail
            elif node.left is not None and node.right is None:
                left_head, left_tail = dfs(node.left)
                node.left = None
                node.right = left_head
                return node,left_tail
            else:
                left_head, left_tail = dfs(node.left)
                right_head, right_tail = dfs(node.right)
                node.left = None
                node.right = left_head
                left_tail.left = None
                left_tail.right = right_head
                return node,right_tail
            
        dfs(root)