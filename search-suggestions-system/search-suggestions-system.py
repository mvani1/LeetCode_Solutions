class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.suggestion = []

    def add_sugestion(self, product):
        if len(self.suggestion) < 3:
            self.suggestion.append(product)
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        root = TrieNode()
        for p in products:
            node = root
            for char in p:
                node = node.children[char]
                node.add_sugestion(p)
        
        result, node = [], root
        for char in searchWord:
            node = node.children[char]
            result.append(node.suggestion)
        return result