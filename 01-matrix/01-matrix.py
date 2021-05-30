class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m,n = len(mat[0]),len(mat)
        queue = deque()
        visited = set()
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    visited.add((i,j))
                    queue.append((i,j))
        while queue:
            old_row,old_col = queue.popleft()
            for x,y in [[-1,0],[0,-1],[1,0],[0,1]]:
                new_r = old_row+x
                new_c = old_col+y
                if new_r>=0 and new_c>=0 and new_r<n and new_c<m and (new_r,new_c) not in visited:
                    mat[new_r][new_c] = mat[old_row][old_col]+1
                    queue.append((new_r,new_c))
                    visited.add((new_r,new_c))
        return mat