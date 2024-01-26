class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    #Double linked list solution
    #Average O(1) time complexity for get and put
    
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.LRU = Node(0,0)
        self.MRU = Node(0,0)
        self.LRU.next = self.MRU
        self.MRU.prev = self.LRU

    def remove(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
        
    def insert(self,node):
        node.next = self.MRU
        self.MRU.prev.next = node
        node.prev = self.MRU.prev
        self.MRU.prev = node
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.cap:
            LRU = self.LRU.next
            del self.cache[LRU.key]
            self.remove(LRU)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)