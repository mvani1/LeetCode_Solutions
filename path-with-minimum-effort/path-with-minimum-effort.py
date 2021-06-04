class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        q = []
        heapq.heappush(q,(0,0,0))
        n,m = len(heights),len(heights[0])
        maxx = float('inf')
        effor = [[maxx]*m for _ in range(n)]
        visited = [[False]*m for _ in range(n)]

        while q :
            r,c,d = heapq.heappop(q)
            if d > effor[r][c] : continue
            if r == n-1 and c == m-1: return d
            for x,y in [(0,1),(1,0),(-1,0),(0,-1)]:
                nr,nc = r+x,y+c
                if 0<=nr<n and 0<=nc<m:
                    nd = max(d,abs(heights[nr][nc]-heights[r][c]))
                    if nd < effor[nr][nc]:
                        effor[nr][nc] = nd
                        heapq.heappush(q,(nr,nc,nd))
        return 0
        