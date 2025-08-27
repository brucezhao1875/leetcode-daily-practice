# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k<=1 : return head
        arr = []
        n = head
        while n is not None:
            t = n
            n = n.next
            t.next = None 
            arr.append(t)

        arr2 = []
        for i in range(len(arr)//k):
            subArr = arr[i*k:(i+1)*k]
            subArr.reverse()
            arr2 += subArr
        # 添加剩余的节点（不足k个的部分）
        remaining = len(arr) % k
        if remaining > 0:
            arr2 += arr[-remaining:]
        
        if not arr2:  # 空数组检查
            return None

        # 重新连接节点
        head = arr2[0]
        for i in range(len(arr2) - 1):  # 注意：i 到 len(arr2)-1
            arr2[i].next = arr2[i + 1]
        arr2[-1].next = None  # 最后一个节点指向 None
        
        return head