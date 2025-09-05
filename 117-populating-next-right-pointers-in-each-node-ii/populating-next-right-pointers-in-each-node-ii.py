"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if not root: return None
        
        def addChilds(q,n):
            if not n : return
            if n.left : q.append(n.left)
            if n.right : q.append(n.right)
        
        q = [root]
        while q:
            q2 = []   #queue for next layer
            x = q[0]
            addChilds(q2,x)
            n = len(q)
            for i in range(1,n):
                x.next = q[i]
                x = x.next
                addChilds(q2,x)
            q = q2
        return root
