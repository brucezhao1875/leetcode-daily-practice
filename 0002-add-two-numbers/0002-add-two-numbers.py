# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(-1)
        p = head
        carry = 0
        while l1 is not None and l2 is not None:
            val = l1.val + l2.val + carry
            if val >= 10 :
                carry = 1
                val = val - 10
            else:
                carry = 0
            
            n = ListNode(val)
            p.next = n
            p = p.next
            l1 = l1.next
            l2 = l2.next

        while l1 is not None:
            val = l1.val + carry
            if val >= 10:
                carry = 1
                val = val - 10
            else:
                carry = 0
            n = ListNode(val)
            p.next = n
            p = p.next
            l1 = l1.next

        while l2 is not None:
            val = l2.val + carry
            if val >= 10:
                carry = 1
                val = val - 10
            else:
                carry = 0
            n = ListNode(val)
            p.next = n
            p = p.next
            l2 = l2.next

        if carry == 1 :
            n = ListNode(1)
            p.next = n
            p = p.next

        return head.next     
        