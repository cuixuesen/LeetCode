class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        if key in self.dict:
            curr_node = self.dict[key]
            self.remove(curr_node)
            self.add(curr_node)
            return curr_node.val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.remove(self.dict[key])
            
        curr_node = Node(key, value)
        self.add(curr_node)
        self.dict[key] = curr_node
        
        if len(self.dict) > self.capacity:
            curr_node = self.head.next
            self.remove(curr_node)
            del self.dict[curr_node.key]
        
    def add(self, node):
        p = self.tail.prev
        p.next = node
        node.prev = p
        node.next = self.tail
        self.tail.prev = node
        
    def remove(self, node):
        node.next.prev, node.prev.next = node.prev, node.next


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)