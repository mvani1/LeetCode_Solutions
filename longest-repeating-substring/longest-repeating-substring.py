class Solution:
    def search(self,L, n, S):
        seen = set()
        for start in range(0, n - L + 1):
            temp = S[start:start+L]
            if temp in seen:
                return start
            seen.add(temp)
        return -1
        
        
    def longestRepeatingSubstring(self, s: str) -> int:
        n = len(s)
        
        left,right = 1, n
        
        while left<=right:
            mid = left + (right-left)//2
            if self.search(mid, n, s) != -1:
                left = mid + 1
            else:
                right = mid - 1
        return left - 1 