# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0,head)
        prev = dummy
        curr = head
        next = head.next if head is not None else None

        while curr is not None and next is not None:
            tmp = next.next
            next.next = curr
            curr.next = tmp
            prev.next = next
            prev = curr
            curr = tmp
            next = tmp.next if tmp is not None else None
        
        return dummy.next
