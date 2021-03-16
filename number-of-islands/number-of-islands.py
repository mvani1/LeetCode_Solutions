class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        self.islands = 0
        for r in range(self.m):
            for c in range(self.n):
                if grid[r][c] == '1':
                    self.islands+=1
                    self.backtrack(grid,r,c)
        return self.islands
    
    def backtrack(self,grid,r,c):
        if r<0 or c<0 or c>=self.n or r>=self.m or grid[r][c]!='1':
            return
        grid[r][c]='0'
        self.backtrack(grid,r+1,c)
        self.backtrack(grid,r-1,c)
        self.backtrack(grid,r,c-1)
        self.backtrack(grid,r,c+1)
        
        