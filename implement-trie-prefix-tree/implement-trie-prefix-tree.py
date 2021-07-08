class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        root = self.trie
        for char in word:
            if char not in root:
                root[char] = {}
            root = root[char]
        root['$'] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        root = self.trie
        for char in word:
            if char not in root:
                return False
            root = root[char]
        return True if root.get('$',False) else False
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        root = self.trie
        for char in prefix:
            root = root.get(char,None)
            if root is None:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)