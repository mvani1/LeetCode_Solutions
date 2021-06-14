class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i in range(len(words)-1):
            for j in range(len(words[i])):
                if j >= len(words[i + 1]): return False
                char1 , char2 = words[i][j], words[i+1][j]
                if words[i][j] != words[i+1][j]:
                    if order.index(char1) > order.index(char2):
                        return False
                    break
        return True