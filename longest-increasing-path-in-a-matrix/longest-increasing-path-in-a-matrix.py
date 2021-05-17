class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        self.N = n
        m = len(matrix[0])
        self.M = m
        self.max = 0
        self.memo = collections.defaultdict(lambda :0)
        for i in range(n):
            for j in range(m):
                self.max = max(self.max,self.longestPath(matrix,i,j,[]))
        return (self.max)
    def longestPath(self,arr,row,col,path):
        path.append(arr[row][col])
        lengthSoFar = len(path)
        temp = lengthSoFar
        if self.memo[(row,col)]:
            return self.memo[(row,col)]
        if row-1>-1 and row-1 <self.N and arr[row-1][col]>arr[row][col]:
            self.memo[(row,col)] = max(self.memo[(row,col)],self.longestPath(arr,row-1,col,path))
            path.pop()
        if row+1>-1 and row+1 <self.N and arr[row+1][col]>arr[row][col]:
            self.memo[(row,col)] = max(self.memo[(row,col)],self.longestPath(arr,row+1,col,path))
            path.pop()

        if col+1>-1 and col+1 <self.M and arr[row][col+1]>arr[row][col]:
            self.memo[(row,col)] = max(self.memo[(row,col)],self.longestPath(arr,row,col+1,path))
            path.pop()
        if col-1>-1 and col-1 <self.M and arr[row][col-1]>arr[row][col]:
            self.memo[(row,col)] = max(self.memo[(row,col)],self.longestPath(arr,row,col-1,path))
            path.pop()
        self.memo[(row,col)] += 1
        return self.memo[(row,col)]
        
            
        

    def valid(self,arr,row,col):
        if row<0 or col<0 or row>=len(arr) or col>=len(arr[0]):
            return False
        return True