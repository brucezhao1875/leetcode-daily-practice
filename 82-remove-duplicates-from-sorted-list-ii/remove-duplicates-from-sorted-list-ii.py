# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        dummy = ListNode(0,head)
        node = dummy
        while node.next and node.next.next:
            if node.next.val == node.next.next.val:
                x = node.next.val
                while node.next and node.next.val == x:
                    node.next = node.next.next
            else:
                node = node.next
        return dummy.next