# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        p,q = l1,l2
        dummy = ListNode()
        n = dummy
        while p or q or carry:
            x = carry
            if p : x += p.val
            if q : x += q.val
            carry = x // 10
            x = x % 10
            n.next = ListNode(x)
            n = n.next
            if p : p = p.next
            if q : q = q.next

        return dummy.next        