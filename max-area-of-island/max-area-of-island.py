class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        self.max = 0
        maxx = 0
        for i in range(n):
            for j in range(m):
                self.max = 0
                if grid[i][j] == 1:
                    self.back(grid,i,j)
                    maxx = max(self.max,maxx)
        return maxx
    def back(self,grid,i,j,max=0):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]!=1:
            return -1
        grid[i][j]=0
        self.max+=1
        # print(max)
        return self.back(grid,i+1,j,max)+\
        self.back(grid,i-1,j,max)+\
        self.back(grid,i,j+1,max)+\
        self.back(grid,i,j-1,max)
        
    