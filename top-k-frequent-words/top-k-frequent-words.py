class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.word = None
        
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        count = collections.Counter(words)
        buckets = [TrieNode() for _ in range(len(words) + 1)]
        for word in count:
            root = buckets[count[word]]
            self.add(word, root)
        
        res = []
        for i in range(len(buckets) - 1, -1, -1):
            if not buckets[i].children:
                continue
            self.getWord(res, buckets[i], k)
            if len(res) >= k:
                return res
        return res
    
    def add(self, word, root):
        for c in word:
            if root.children[ord(c) - ord("a")] == None:
                root.children[ord(c) - ord("a")] = TrieNode()
            root = root.children[ord(c) - ord("a")]
        root.word = word
        
        
    def getWord(self, res, root, k):
        if not root:
            return 
        if len(res) >= k:
            return 
        if root.word:
            res.append(root.word)
        
        for i in range(26):
            self.getWord(res, root.children[i], k)
        return 