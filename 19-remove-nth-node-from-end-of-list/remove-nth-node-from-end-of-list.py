# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(val=0,next=head)
        
        p = dummy
        q = p
        for i in range(n):
            q = q.next
        
        while q is not None and q.next is not None:
            p = p.next
            q = q.next
        
        p.next = p.next.next
    
        return dummy.next
        