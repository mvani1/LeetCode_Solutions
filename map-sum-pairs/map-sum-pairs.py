class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        self.map = {}

    def insert(self, key: str, val: int) -> None:
        delta = val - self.map.get(key,0)
        curr = self.trie
        self.map[key] = val
        for char in key:
            if char not in curr:
                curr[char] = {}
            curr = curr[char]
            curr['$'] = curr.get('$',0)+delta

    def sum(self, prefix: str) -> int:
        curr = self.trie
        for char in prefix:
            if char not in curr:
                return 0 
            curr = curr[char]
        if '$' in curr:
            return (curr['$'])
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)