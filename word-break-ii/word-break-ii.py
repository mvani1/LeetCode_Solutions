class TrieNode:
    def __init__(self, val, isWord=False):
        self.val = val
        self.isWord = isWord
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode(None)

    def insert(self, word):
        if not word:
            return

        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode(char)
            curr = curr.children[char]
        curr.isWord = True
        

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        sol = Trie()
        for word in wordDict:
            sol.insert(word)
            
        return self.walk(s, sol.root, {})

    def walk(self, seq, root, memo):
        if not seq:
            return ['']
        if seq in memo:
            return memo[seq]

        # Find all the words we can get from the beginning of seq
        # E.g. for 'catsanddogs', this would be ['cat', 'cats']
        words = []  
        curr = root
        for idx, char in enumerate(seq):
            if char not in curr.children:
                break
            curr = curr.children[char]
            if curr.isWord:
                # Break point
                words.append(seq[: idx + 1])

        fragments = []
        for word in words:
            # Recurse using substring of seq after word,
            # which is necessarily a prefix.
            # E.g. if seq=`catsanddogs` and word=`cats`,
            # recursive with seq'='anddogs'.
            rest_of_sentence_endings = self.walk(
                seq[len(word) :], root, memo
            )
            # Join each of the returned setence endings to
            # create a new, longer set of sentence endings.
            for sentence_ending in rest_of_sentence_endings:
                if sentence_ending:
                    fragments.append(' '.join([word, sentence_ending]))
                else:
                    fragments.append(word)

        memo[seq] = fragments
        return memo[seq]