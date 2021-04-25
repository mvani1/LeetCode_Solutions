class Solution:
    def exist(self, grid: List[List[str]], word: str) -> bool:
        self.word = word
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == word[0]:
                    if self.dfs(i,j,grid,0): return True
        return False
                    
    def dfs(self,x,y,grid,index):
        if index == len(self.word): return True
        
        if x == -1 or y == -1 or x == len(grid) or y == len(grid[0]) \
        or self.word[index] != grid[x][y]:
            return False
        
        char = grid[x][y]
        grid[x][y] = 0
        index += 1
        try:
            return self.dfs(x+1,y,grid,index) or \
            self.dfs(x-1,y,grid,index) or \
            self.dfs(x,y-1,grid,index) or \
            self.dfs(x,y+1,grid,index)
        finally:
            grid[x][y] = char

            