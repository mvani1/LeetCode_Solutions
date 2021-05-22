import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self._map: Dict[int] = {}
        self._array: Array[int] = []
        self.length = 0
    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self._map:
            return False
        
        self._map[val] = self.length
        self._array.append(val)
        self.length +=1
        return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self._map:
            return False
        
        last_element, idx_val = self._array[-1], self._map[val]
        self._array[idx_val], self._map[last_element] = last_element, idx_val
        
        
        self._array.pop()
        del self._map[val]
        self.length -=1
        return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self._array)