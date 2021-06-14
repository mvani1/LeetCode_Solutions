class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.o = defaultdict(list)
        for i,v in enumerate(wordsDict):
            self.o[v].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        minn = float('inf')
        # print(self.o[word1],self.o[word2])
        for i in self.o[word1]:
            for j in self.o[word2]:
                minn = min(abs(i-j),minn)
        return minn

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)