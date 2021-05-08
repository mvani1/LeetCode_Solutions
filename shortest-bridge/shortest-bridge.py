class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        n,m = len(A),len(A[0])
        stack = []
        flag = 0
        directions = {(1,0),(0,1),(-1,0),(0,-1)}
        for i in range(n):
            for j in range(m):
                if A[i][j] == 1:
                    flag = 1
                    self.dfs(i,j,A,stack)
                    break
            if flag == 1:
                break
        steps = 0
        # -----------
        # breadth first search, once we find next '1', that is our final answer 
        # -----------
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while stack:
            size = len(stack)
            level = []
            while(size):
                temp = stack.pop()
                size-=1
                x, y = temp[0], temp[1]
                for dx, dy in dirs:
                    tx = x+dx
                    ty = y+dy
                    if tx<0 or ty<0 or tx>=n or ty>=m or A[tx][ty]==2:
                        continue
                    if A[tx][ty]==1:
                        return steps
                    A[tx][ty]=2
                    level.append((tx, ty))
            steps+=1
            stack = level
        return -1 
        flips = 0
        while self.stack:
            level = []
            for i,j in self.stack:
                for x,y in directions:
                    newX,newY = i+x,j+y
                    if newX <0 or newY<0 or newX>=n or newY>=m or A[newX][newY]==2:
                        continue
                    if A[newX][newY] == 1:
                        return flips
                    A[newX][newY] = 2
                    level.append((newX,newY))
                flips +=1
                self.stack = level
        return -1
            
        
    def dfs(self,row,col,A,stack):
        if row<0 or col <0 or row>= len(A) or col >=len(A[0]) or A[row][col]!=1:
            return
        A[row][col] = 2
        stack.append((row,col))
        self.dfs(row-1,col,A,stack)
        self.dfs(row,col-1,A,stack)
        self.dfs(row,col+1,A,stack)
        self.dfs(row+1,col,A,stack)
