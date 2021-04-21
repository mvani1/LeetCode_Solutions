class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        queue = deque()
        fresh_oranges = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    fresh_oranges+=1
        queue.append((-1,-1))
        minutes_elapsed = -1
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        while queue:
            row,col = queue.popleft()
            if row == -1:
                minutes_elapsed +=1
                if queue:
                    queue.append((-1,-1))
            else:
                for r,c in directions:
                    n_row,n_col = row+r,col+c
                    
                    if n>n_row>=0 and m>n_col>=0:
                        if grid[n_row][n_col] == 1:
                            grid[n_row][n_col] = 2
                            fresh_oranges-=1
                            queue.append((n_row,n_col))
        return minutes_elapsed if fresh_oranges == 0 else -1