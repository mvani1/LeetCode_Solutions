class Solution:
    def trailingZeroes(self, n: int) -> int:
        def fact(n):
            if n ==0 or n==1:
                return 1
            # print(n)
            return n*fact(n-1)
        n = (fact(n))
        # print(n)
        return len(str(n))-len(str(n).strip('0'))
        