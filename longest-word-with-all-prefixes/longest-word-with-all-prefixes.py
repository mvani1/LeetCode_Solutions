class Node:
    def __init__(self):
        self.children = {}
        self.string = ''

class Solution:
    def longestWord(self, words: List[str]) -> str:
        self.root = Node()
        self.ans = ''
        for word in words:
            self.insert(word)
        for word in words:
            self.find(word)
        return self.ans
        
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
        node.string = word
    
    def find(self, word):
        node = self.root
        for c in word:
            node = node.children[c]
            if not node.string:
                return
        if len(word) > len(self.ans):
            self.ans = word
        elif len(word) == len(self.ans) and word < self.ans:
            self.ans = word