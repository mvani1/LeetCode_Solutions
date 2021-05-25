class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        R = len(matrix)
        C = len(matrix[0])
        def recursion(matrix,x,y,memo):
            if x<0 or y <0 or x>=R or y>=C or matrix[x][y]!=1:
                return 0
            if memo[x][y]:return memo[x][y]
            ans = 0
            down = recursion(matrix,x+1,y,memo)
            right = recursion(matrix,x,y+1,memo)
            diag = recursion(matrix,x+1,y+1,memo)
            ans = min(down,min(right,diag)) + 1
            memo[x][y] = ans
            return ans
        
        ans = 0
        memo = [[0]*C for _ in range(R)]
        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 1:
                    ans += recursion(matrix,i,j,memo)

        return ans