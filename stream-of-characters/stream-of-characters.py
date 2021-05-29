class StreamChecker:

    def __init__(self, words: List[str]):
        '''
        Time = Space = O(N.M)
        where N is the number of input word and M is the word Length
        '''
        self.trie = {}
        self.stream = deque([])
        
        for word in set(words):
            node = self.trie
            for char in word[::-1]:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node['#'] = word

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        
        node = self.trie
        
        for char in self.stream:
            if '#' in node:
                return True
            if char not in node:
                return False
            
            node = node[char]
        return '#' in node


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)