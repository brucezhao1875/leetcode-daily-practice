# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge_two_list(a,b):
            if a is None : return b
            if b is None : return a
            dummy = ListNode(-1)
            p = dummy
            while a and b:
                if a.val < b.val:
                    p.next = a
                    a = a.next
                else:
                    p.next = b
                    b = b.next
                p = p.next
            p.next = a if a else b
            return dummy.next
        def merge(lists: list , l: int, r: int) :
            if l == r : return lists[l]
            if l > r : return None
            mid = (l+r) // 2
            return merge_two_list(merge(lists,l,mid),merge(lists,mid+1,r))

        return merge(lists,0,len(lists)-1)