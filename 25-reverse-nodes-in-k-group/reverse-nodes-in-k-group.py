# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr = []
        p = head
        while p:
            t = p
            p = p.next
            t.next = None
            arr.append(t)
        n = len(arr)
        loops = n // k
        start = 0
        for loop in range(loops):
            start = k*loop
            end = k*(loop+1) - 1
            while start < end:
                t = arr[start]
                arr[start] = arr[end]
                arr[end] = t
                start += 1
                end -= 1
        
        for i in range(n-1):
            arr[i].next = arr[i+1]
        
        return arr[0]

    #如下方法其实才是出题者想要的想法，哈哈哈
    def reverseKGroup2(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        
        while True:
            # 检查是否还有k个节点
            kth = prev
            for i in range(k):
                kth = kth.next
                if kth is None:
                    return dummy.next
            
            # kth现在指向第k个节点
            next_group = kth.next  # 保存下一组的起始位置
            
            # 反转当前组的k个节点
            # 使用标准的反转链表方法
            prev_node = next_group
            curr = prev.next
            
            # 反转k个节点
            for i in range(k):
                next_temp = curr.next
                curr.next = prev_node
                prev_node = curr
                curr = next_temp
            
            # 连接反转后的组
            # prev_node现在指向反转后的第一个节点（原来的第k个）
            # prev.next原来指向组的第一个节点，现在应该指向反转后的第一个
            temp = prev.next
            prev.next = prev_node
            prev = temp  # 更新prev为原来的第一个节点（现在是组的最后一个）