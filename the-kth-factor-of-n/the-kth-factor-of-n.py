class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        self.k = k
        return self.print_factors(n)
    def print_factors(self,x):
        for i in range(1, x + 1):
            if x % i == 0:
                self.k-= 1
            if self.k == 0:
                return i
            
        return -1
