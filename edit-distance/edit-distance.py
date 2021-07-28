class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        self.memo = {}
        return self.minn(word1,word2)
    def minn(self,word1,word2):
        if (word1,word2) in self.memo:
            return self.memo[(word1,word2)]
        if not word1 and not word2:
            return 0
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        if word1[0] == word2[0]:
            return self.minn(word1[1:],word2[1:])
        insert = self.minn(word1,word2[1:])+1
        delete = self.minn(word1[1:],word2)+1
        replace =self.minn(word1[1:],word2[1:])+1
        ans = min(insert,replace,delete)
        self.memo[(word1,word2)] = ans
        return ans