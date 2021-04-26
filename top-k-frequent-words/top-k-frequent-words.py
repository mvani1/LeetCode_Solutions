class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = ''
        self.freq = 0
        
    def __lt__(self, other):
        return self.freq > other.freq if self.freq != other.freq else self.word < other.word

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        root = self.root
        for c in word:
            if c not in root.children:
                root.children[c] = TrieNode()
            root = root.children[c] 
        root.is_word = True
        root.word = word
        root.freq += 1
    
    def topK(self, k):
        q, pq = collections.deque([self.root]), []
        while q:
            node = q.popleft()
            if node.is_word: heapq.heappush(pq, node)
            for _, nxt in node.children.items():
                q.append(nxt)
        return heapq.nsmallest(k, pq)

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        trie = Trie()
        for w in words:
            trie.insert(w)
        return [node.word for node in trie.topK(k)]