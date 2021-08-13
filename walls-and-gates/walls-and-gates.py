class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        INF = 2147483647
        q = deque()
        n,m = len(rooms),len(rooms[0])
        for i in range(n):
            for j in range(m):
                if rooms[i][j] == 0:
                    q.append((i,j))
        
        while q :
            x,y = q.popleft()
            for xx,yy in directions:
                new_x,new_y = xx+x, yy+y
                if new_x<0 or new_y<0 or new_x>=n or new_y>=m or rooms[new_x][new_y]!=INF:
                    continue
                rooms[new_x][new_y] = rooms[x][y] + 1
                q.append((new_x,new_y))
                    
