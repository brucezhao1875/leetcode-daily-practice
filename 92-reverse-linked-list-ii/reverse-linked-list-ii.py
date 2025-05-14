# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 迭代法有点有意思的细节；就陪着玩玩吧！
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def reverse(head):
            prev = None
            curr = head
            while curr :
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            return prev

        def split(head,left,right):
            p,q,r = ListNode(),ListNode(),ListNode()
            n = p
            for i in range(1,left):
                n.next = ListNode(head.val)
                n = n.next
                head = head.next
            n = q
            for i in range(right- left + 1):
                n.next = ListNode(head.val)
                n = n.next
                head = head.next
            r.next = head

            return p.next,q.next,r.next
        
        def merge(p,q,r):
            dummy = ListNode()
            n = dummy
            while p :
                n.next = ListNode(p.val)
                n = n.next
                p = p.next
            while q :
                n.next = ListNode(q.val)
                n = n.next
                q = q.next
            while r :
                n.next = ListNode(r.val)
                n = n.next 
                r = r.next
            return dummy.next
        
        p,q,r = split(head,left,right)
        return merge(p,reverse(q),r)