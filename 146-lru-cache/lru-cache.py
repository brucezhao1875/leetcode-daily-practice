class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.data = {}
        self.capacity = capacity
    def get(self, key: int) -> int:
        node = self.data.get(key)
        if node is None:
            return -1
        self.remove_from_list(node)
        self.add_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.data.get(key)
        if node is None:
            if len(self.data) >= self.capacity:
                x = self.tail.prev
                self.remove_from_list(x)
                del self.data[x.key]
            x = Node(key,value)
            self.add_to_head(x)
            self.data[x.key] = x
        else:
            node.value = value
            self.remove_from_list(node)
            self.add_to_head(node)
    
    def add_to_head(self,node) -> None:
        tmp = self.head.next 
        self.head.next = node
        node.next = tmp
        tmp.prev = node
        node.prev = self.head
    def remove_from_list(self,node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)