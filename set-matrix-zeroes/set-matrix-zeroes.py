class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    row.add((i,j))
        for i,v in row:
            for k in range(len(matrix[0])):
                matrix[i][k] = 0
        
        for i,v in row:
            for k in range(len(matrix)):
                matrix[k][v] = 0
        
        