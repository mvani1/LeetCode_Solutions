class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        word_len =0
        for i in sentences:
            if len(i.split(" ")) > word_len:
                word_len = len(i.split(" "))
            
        return (word_len)
           