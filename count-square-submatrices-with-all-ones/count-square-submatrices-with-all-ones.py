class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        R = len(matrix)
        C = len(matrix[0])
        ans = 0
        for i in range(1,R):
            for j in range(1,C):
                if not matrix[i][j]:continue
                if matrix[i-1][j] and matrix[i][j-1] and matrix[i-1][j-1]: 
                    matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + 1
        return sum(map(sum, matrix))