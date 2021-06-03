class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        n,m = len(grid),len(grid[0])
        queue = deque([[0,0,0,k]])
        trackLives = [[-1]*m for i in range(n)]
        while queue:
            cr,cc,cdist,lives = queue.popleft()
            if cr == n-1 and cc == m-1:
                return cdist
            if grid[cr][cc] == 1:
                lives-=1
            
            for d in [(0,1),(1,0),(-1,0),(0,-1)]:
                nr,nc = cr+d[0],cc+d[1]
                if 0 <= nr < n and 0 <= nc < m and trackLives[nr][nc]<lives:
                    queue.append([nr,nc,cdist+1,lives])
                    trackLives[nr][nc] = lives
        return -1