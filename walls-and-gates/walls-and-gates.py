class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        if not rooms: return
        q = []
        m, n = len(rooms), len(rooms[0])
        for i in range(m):
            for j in range(n):
                if not rooms[i][j]:
                    q.append((i, j))
        dis = 1                    
        while q:
            tmp_q = []
            while q:
                i, j = q.pop()
                for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    ii, jj = i+di, j+dj
                    if 0 <= ii < m and 0 <= jj < n and rooms[ii][jj] == 2147483647:
                        rooms[ii][jj] = dis 
                        tmp_q.append((ii, jj))
            q = tmp_q             
            dis += 1