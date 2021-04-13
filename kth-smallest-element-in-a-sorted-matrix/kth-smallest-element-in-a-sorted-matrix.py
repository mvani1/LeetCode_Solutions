class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m = []
        for i in matrix:
            m.extend(i)
        m.sort()
        return m[k-1]