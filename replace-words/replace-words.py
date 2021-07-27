class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = {}
        result = []
        
        for word in dictionary:
            root = trie
            for char in word:
                if not (char in root):
                    root[char] = {}
                root = root[char]
            root['$'] = word
        
        for i in sentence.split():
            root = trie
            flag = 0
            for char in i:
                if char not in root:
                    break
                root = root[char]
                if '$' in root:
                    result.append(root['$'])
                    flag = 1
                    break
            if not flag:
                result.append(i)
        return " ".join(result)
        