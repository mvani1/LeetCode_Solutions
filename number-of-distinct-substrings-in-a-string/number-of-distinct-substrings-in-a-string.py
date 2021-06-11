class Solution:
    def countDistinct(self, s: str) -> int:
        trie = {}
        res = 0
        for i in range(len(s)):
            cur = trie
            for j in range(i, len(s)):
                if s[j] not in cur:
                    cur[s[j]] = {}
                    res += 1
                cur = cur[s[j]]
        print(trie)
        return res