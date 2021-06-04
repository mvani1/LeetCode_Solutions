from collections import Counter
class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        row = len(mat)
        col = len(mat[0])
        maxx = 0
        for i in range(row):
            #horizontal
            count = 0
            for j in range(col):
                if mat[i][j] == 1:
                    count += 1
                else:
                    maxx = max(maxx,count)
                    count = 0
            maxx = max(maxx,count)
            
        for j in range(col):
            # vertical
            count = 0
            for i in range(row):
                if mat[i][j] == 1:
                    count += 1
                else:
                    maxx = max(maxx,count)
                    count = 0
            maxx = max(maxx,count)
                    
        for i in range(row):
            # diagonal
            for j in range(col):
                o = j+1
                count = 0
                if mat[i][j] == 1:
                    count += 1
                    for k in range(i+1,row):
                        
                        if o<col and mat[k][o] == 1:
                            count += 1
                        else:
                            break
                        o+=1
                        # print(count)
                maxx = max(maxx,count)
        
        for i in range(row):
            # anti-diagonal
            for j in range(col):
                o = j-1
                count = 0
                if mat[i][j]==1:
                    count+=1
                    for k in range(i+1,row):
                        # print(i,j,k,o)
                        if o >-1 and mat[k][o] == 1:
                            count += 1
                        else:
                            break
                        o-=1
                maxx = max(maxx,count)
        print(maxx)
                    
        return (maxx)
