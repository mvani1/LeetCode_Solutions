class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {u:[] for u in range(n)}
        for f in flights:
            adj[f[0]].append((f[1],f[2]))
        print(adj)
        h = []
        h.append((0,src,k+1))
        
        while h:
            top = heapq.heappop(h)
            currcost,currvertex,e = top
            if currvertex == dst:
                return currcost
            if e>0:
                for neigh,neighcost in adj[currvertex]:
                    heapq.heappush(h,(currcost+neighcost,neigh,e-1))
        return -1       