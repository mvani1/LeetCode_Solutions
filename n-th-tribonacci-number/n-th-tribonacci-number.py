class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n
        if n == 2:
            return 1
        cache = [0] * (n+1)
        cache[1] = cache[2] = 1
        
        # formula = self.tribonacci(n-3) +  self.tribonacci(n-2) +  self.tribonacci(n-1)
        for i in range(3,n+1):
            cache[i] = cache[i-3]+cache[i-2]+cache[i-1]
        return cache[n]