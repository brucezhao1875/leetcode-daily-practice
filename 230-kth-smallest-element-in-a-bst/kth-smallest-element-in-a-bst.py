# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
        这把它遍历出来，然后取第k个，不就可以了吗?
        '''
        array = []
        def traverse(node : Optional[TreeNode],result) -> List[int]:
            if node is not None :
                traverse(node.left,array)
                array.append(node.val)
                traverse(node.right,array)

        traverse(root,array)
        #print(array)
        return array[k-1]