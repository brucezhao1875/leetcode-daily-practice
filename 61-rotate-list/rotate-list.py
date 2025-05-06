# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None : return head
        nodes = []
        while head:
            next = head.next
            head.next = None
            nodes.append(head)
            head = next
        
        n = len(nodes)
        k = k % n 
        nodes = nodes[n-k:n] + nodes[0:n-k]

        for i in range(n-1):
            nodes[i].next = nodes[i+1]
        return nodes[0]
        