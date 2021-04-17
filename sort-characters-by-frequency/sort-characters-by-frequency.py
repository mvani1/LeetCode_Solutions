class Solution:
    def frequencySort(self, s: str) -> str:
        freq = collections.Counter(s)
        return "".join(sorted(s,key=lambda x : (-freq[x],x)))