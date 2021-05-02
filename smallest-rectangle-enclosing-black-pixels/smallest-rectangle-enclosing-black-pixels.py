class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        self.row = []
        self.col = []
        self.dfs(image,x,y)
        print(self.row,self.col)
        size1 = max(self.row)-min(self.row)+1
        size2 = max(self.col)-min(self.col)+1
        return size1*size2
        
    def dfs(self,image,x,y):
        if x<0 or y<0 or x>=len(image) or y>=len(image[0]) or image[x][y]!="1":
            return 
        if image[x][y]=="1":
            self.row.append(x)
            self.col.append(y)
        image[x][y] = '#'
        self.dfs(image,x-1,y)
        self.dfs(image,x+1,y)
        self.dfs(image,x,y+1)
        self.dfs(image,x,y-1)
        # image[x][y]=1
        