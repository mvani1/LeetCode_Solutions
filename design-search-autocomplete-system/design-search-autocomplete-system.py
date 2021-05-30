class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = {}
        self.sentences = sentences
        self.keyword = ''
        self.times = times
    
        for i in range(len(sentences)):
            self._build(sentences[i],times[i])
            
    def _build(self,sentence,time):
        node = self.trie
        for char in sentence:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['data'] = sentence
        node['isEnd'] = True
        node['rank'] = node.get('rank',0) - time

    def search(self,words):
        node = self.trie
        for word in words:
            if word not in node:
                return []
            node = node[word]
        return self.dfs(node)
    
    def dfs(self,node):
        ret = []
        if node and type(node)==dict:
            if node.get('isEnd',0):
                ret.append((node['rank'],node['data']))
            for child in node:
                ret.extend(self.dfs(node[child]))
        return ret
        

    def input(self, c: str) -> List[str]:
        suggestions = []
        if c!='#':
            self.keyword += c
            suggestions = self.search(self.keyword)
        else:
            self._build(self.keyword,1)
            self.keyword = ''
        return [item[1] for item in sorted(suggestions)[:3]]


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)