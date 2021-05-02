class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        self.cache = defaultdict(int)
        n = len(obstacleGrid) - 1
        m = len(obstacleGrid[0]) - 1
        if obstacleGrid[0][0] or obstacleGrid[n][m] : return 0
        
        return self.recursive(n, m, obstacleGrid)
        return (self.cache[(n,m)])
    
    def recursive(self,currRow, currCol, board):
        if currRow < 0 or currCol < 0:
            return 0
        
        if currRow == 0 and currCol == 0:
            return 1
        if board[currRow][currCol] : return 0
        
        if self.cache[(currRow, currCol)] : return self.cache[(currRow, currCol)]
        
        self.cache[(currRow, currCol)] = self.recursive(currRow -1, currCol, board) + self.recursive(currRow, currCol - 1, board)
        
        return self.cache[(currRow, currCol)]
        