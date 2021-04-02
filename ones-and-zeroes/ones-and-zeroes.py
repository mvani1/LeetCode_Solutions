class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        M=m
        N=n
        dp = [[0 for _ in range(N+1)] for _ in range(M+1)]
        S=strs
        for str in S:
            zeros = str.count("0")
            ones = len(str) - zeros
            for i in range(M, zeros - 1, -1):
                for j in range(N, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-zeros][j-ones] + 1)
        return dp[M][N]