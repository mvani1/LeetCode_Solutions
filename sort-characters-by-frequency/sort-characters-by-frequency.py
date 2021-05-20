class Solution:
    

    def frequencySort(self, s: str) -> str:
        c = collections.Counter(s)
        
        finalStr = ""
        for e in c.most_common():
            
            finalStr += e[0] * e[1]
            
        return finalStr