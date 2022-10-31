class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxNumberOfWords = 0
        for sentence in sentences:
            maxNumberOfWords = max(maxNumberOfWords, len(sentence.split()))
        return maxNumberOfWords
           