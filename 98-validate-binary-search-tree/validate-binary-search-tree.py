# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        array = []
        def traverse(node,array):
            if node is not None:
                traverse(node.left,array)
                array.append(node.val)
                traverse(node.right,array)

        traverse(root,array)

        if len(array) <= 1 : return True
        for i in range(len(array)-1):
            if array[i]>=array[i+1] : 
                return False
        return True
