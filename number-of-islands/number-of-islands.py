class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.m,self.n = len(grid),len(grid[0])
        count = 0
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == "1" :
                    self.dfs(grid,i,j)
                    count+=1
        return count
    def dfs(self, grid, x, y):
        grid[x][y]='X'
        if x+1<self.m and grid[x+1][y] == "1": self.dfs(grid,x+1,y)
        if y+1<self.n and grid[x][y+1] == "1": self.dfs(grid,x,y+1)            
        if x-1>=0 and grid[x-1][y] == "1": self.dfs(grid,x-1,y)            
        if y-1>=0 and grid[x][y-1] == "1": self.dfs(grid,x,y-1)            
