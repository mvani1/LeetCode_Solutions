class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row = []
        for i in range(len(grid)):
            row.append(max(grid[i]))
        col = []
        maxx = 0
        for j in range(len(grid[0])):
            maxx =0 
            for i in range(len(grid)):
                if maxx<=grid[i][j]:
                    maxx =grid[i][j]
            col.append(maxx)
            
        res = 0 
        for i in range(len(grid)):
            minn = 0
            for j in range(len(grid[0])):
                minn = min(col[i],row[j])
                res += abs(minn-grid[j][i])
                grid[j][i] = minn
        return res
            
        