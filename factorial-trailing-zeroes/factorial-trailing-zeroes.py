class Solution:
    def trailingZeroes(self, n: int) -> int:
        # memo = []
        def fact(n):
            if n ==0 or n==1:
                return 1
            return n*fact(n-1)
        n = (fact(n))
        
        return len(str(n))-len(str(n).strip('0'))
        