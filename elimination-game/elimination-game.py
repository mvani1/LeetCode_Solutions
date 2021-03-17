class Solution:
    def lastRemaining(self, n: int) -> int:
        return 1 if n==1 else (n//2 - self.lastRemaining(n//2)+1)*2