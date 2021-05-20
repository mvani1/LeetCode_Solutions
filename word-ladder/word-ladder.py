from collections import defaultdict, deque


class Trie:
    def __init__(self):
        def trie_factory():
            return defaultdict(trie_factory)

        self.root = defaultdict(trie_factory)

    def add(self, s):
        node = self.root
        for c in s:
            node = node[c]

        node['$'] = s

    def findBy(self, s, total_changes=0):
        t = []

        n = len(s)

        def search(i, node, changes_left):
            if i == n:
                if '$' in node:
                    t.append(node['$'])

                return

            if not changes_left:
                if s[i] in node:
                    search(i + 1, node[s[i]], 0)
            else:
                for c in string.ascii_lowercase:
                    if c in node:
                        search(i + 1, node[c], changes_left - (1 if c != s[i] else 0))

        search(0, self.root, total_changes)

        return t


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        trie = Trie()

        for word in wordList:
            trie.add(word)

        q = deque()
        seen = set()

        q.append((beginWord, 1))

        while q:
            word, k = q.popleft()

            if word in seen:
                continue

            if word == endWord:
                return k

            seen.add(word)

            for nextWord in trie.findBy(word, 1):
                if nextWord not in seen:
                    q.append((nextWord, k + 1))

        return 0