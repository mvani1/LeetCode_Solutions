class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key_range = 769
        self.bucket_array = [Bucket() for i in range(self.key_range)]
    
    def _hash(self, key):
        return key % self.key_range
    
    def add(self, key: int) -> None:
        bucketIndex = self._hash(key)
        self.bucket_array[bucketIndex].insert(key)

    def remove(self, key: int) -> None:
        bucketIndex = self._hash(key)
        self.bucket_array[bucketIndex].delete(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        bucketIndex = self._hash(key)
        return self.bucket_array[bucketIndex].exists(key)
        
class Node:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.next = nextNode

class Bucket:
    def __init__(self):
        self.head = Node(0)
    
    def insert(self, value):
        if not self.exists(value):
            new_node = Node(value,self.head.next)
            self.head.next = new_node
    
    def delete(self, value):
        prev = self.head
        curr = self.head.next
        while curr:
            if value == curr.value:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next
            
    def exists(self, value: int) -> bool:
        curr = self.head.next
        while curr:
            if curr.value == value:
                return True
            curr = curr.next
        return False
        
    

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)