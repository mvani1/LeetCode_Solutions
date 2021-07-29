class Solution:
    def findLucky(self, arr: List[int]) -> int:
        result = -1
        freq = Counter(arr)
        print(freq)
        for k in set(arr):
            if k==freq.get(k):
                result = k
        return result