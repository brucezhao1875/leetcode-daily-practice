# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        array_left = []
        array_right = []
        p = head
        while p:
            if p.val >= x:
                array_right.append(p)
            else:
                array_left.append(p)
            p = p.next

        array = [ListNode(0)] + array_left + array_right

        for i in range(len(array)-1):
            array[i].next = array[i+1]
        array[-1].next = None        
        return array[0].next