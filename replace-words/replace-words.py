class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        Trie = lambda: defaultdict(Trie)
        trie = Trie()
        END = True
        
        for dictt in dictionary:
            reduce(dict.__getitem__,dictt,trie)[END] = dictt
        def replace(word):
            node = trie
            for char in word:
                if char not in node or END in node:break
                node = node[char]
            return node.get(END,word)
        
        return " ".join(map(replace,sentence.split()))
            