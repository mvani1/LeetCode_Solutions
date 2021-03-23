class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix is None:return 
        
        rows,cols = len(matrix),len(matrix[0])
        dp = [[0]*(cols+1) for _ in range(rows+1)]
        maxx = 0
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c]=='1':
                    dp[r][c] = min(dp[r-1][c],dp[r-1][c-1],dp[r][c-1]) + 1
                    maxx = max(maxx,dp[r][c])
        return maxx*maxx