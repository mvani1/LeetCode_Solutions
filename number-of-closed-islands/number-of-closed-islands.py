class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        '''
        CHange all the 0 to -1 and the global variable 
        Time = O(n*m) 
        Space = O(1)
        '''
        m, n = len(grid), len(grid[0])
        res = 0
        
        def dfs(x, y):
            if x in (0, m-1) or y in (0, n-1):
                self.isIsland = False 
            for i, j in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                if 0 <= i < m and 0 <= j < n and grid[i][j] == 0:
                    grid[i][j] = -1 
                    dfs(i, j)
                    
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    self.isIsland = True
                    dfs(i, j)
                    res += self.isIsland
                    
        return res 