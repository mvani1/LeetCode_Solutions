class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.n,self.m = len(grid),len(grid[0])
        self.seen = set()
        self.grid = grid
        count = 0
        for i in range(self.n):
            for j in range(self.m):
                if grid[i][j] == "1" and (i,j) not in self.seen:
                    self.dfs(i,j)
                    count+=1
        return count
    def dfs(self, x, y):
        if x<0 or y<0 or x>=self.n or y>=self.m or self.grid[x][y]!="1" or (x,y) in self.seen:
            return
        self.seen.add((x,y))
        for xx,yy in [[0,1],[1,0],[-1,0],[0,-1]]:
            new_x,new_y = x+xx,y+yy
            self.dfs(new_x,new_y)
    
        