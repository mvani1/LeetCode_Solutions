class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        #find Location
        n,m = len(grid),len(grid[0])
        start = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '*':
                    start = (i,j)
        length = 0
        minn = float('inf')
        q = deque([(start,length)])
        seen = set()
        while q:
            # print(q)
            size = len(q)
            for i in range(size):
                coord,steps = q.popleft()
                x,y = coord
                if grid[x][y] == '#':
                    return steps
                for i,j in [(0,1),(1,0),(0,-1),(-1,0)]:
                    newX,newY = x+i,y+j
                    newCoor = (newX,newY)
                    if 0 <= newX < n and 0 <= newY < m and grid[newX][newY]!='X' and (newX,newY) not in seen:
                        q.append((newCoor,steps+1))
                        seen.add(newCoor)
        
        if minn !=inf:
            return minn
        return -1

                    