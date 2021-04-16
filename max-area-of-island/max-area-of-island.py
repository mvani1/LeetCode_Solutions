class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:return 0
        self.area = 0
        def back(x,y,grid):
            self.area+=1
            grid[x][y] ='-1'
            if x+1<len(grid) and grid[x+1][y]==1:
                back(x+1,y,grid)
            if x-1<len(grid) and x-1>-1 and grid[x-1][y]==1:
                back(x-1,y,grid)
            if y-1<len(grid[0]) and y-1>-1 and grid[x][y-1]==1:
                back(x,y-1,grid)
            if y+1<len(grid[0]) and grid[x][y+1]==1:
                back(x,y+1,grid)
            
        maxx=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    back(i,j,grid)
                    maxx = max(maxx,self.area)
                    self.area = 0
                    
        return(maxx)