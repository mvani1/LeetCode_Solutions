class Solution:
    def exist(self, grid: List[List[str]], word: str) -> bool:
        self.word = word
        self.rows = len(grid)
        self.cols = len(grid[0])
        all_chars = set(word)
        
        for i in range(self.rows):
            for j in range(self.cols):
                if grid[i][j] in all_chars:
                    all_chars.remove(grid[i][j])
                    
		# exit if missing any character
        if all_chars: return False
        
        for i in range(self.rows):
            for j in range(self.cols):
                if self.dfs(i,j,grid,0): return True
        return False
                    
    def dfs(self,x,y,grid,index):
        if index == len(self.word): return True
        
        if x == -1 or y == -1 or x == self.rows or y == self.cols \
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

            