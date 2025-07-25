# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {k:v for v,k in enumerate(inorder)}
        self.postorder_idx = len(postorder) - 1 
        
        def build(left,right):
            if left > right : return None
            
            root_val = postorder[self.postorder_idx]
            self.postorder_idx -= 1
            inorder_idx = inorder_map[root_val]
            right = build(inorder_idx+1,right)
            left = build(left,inorder_idx-1)
            root = TreeNode(root_val,left,right)
            return root
        
        return build(0,len(inorder)-1)
            