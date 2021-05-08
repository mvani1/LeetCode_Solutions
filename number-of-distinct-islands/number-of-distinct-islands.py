class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        distinct_row = set()
        for row in range(n):
            for col in range(m):
                if grid[row][col] == 1:
                    path = self.dfs(grid,row,col,n,m,'X')
                    distinct_row.add(path)
        ans = len(distinct_row)
        return ans
    def dfs(self,grid,row,col,n,m,start):
        if not self.valid(grid,row,col,n,m): return 'O'
        grid[row][col] = 0
        return start + self.dfs(grid,row-1,col,n,m,'U')+\
        self.dfs(grid,row+1,col,n,m,'D')+\
        self.dfs(grid,row,col-1,n,m,'L')+\
        self.dfs(grid,row,col+1,n,m,'R')
    def valid(self,grid,row,col,n,m):
        if row<0 or col <0 or row>=n or col>=m or grid[row][col]!=1:
            return False
        return True
        