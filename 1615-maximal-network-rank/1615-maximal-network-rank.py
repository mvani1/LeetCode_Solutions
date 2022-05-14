class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adj = {_:[] for _ in range(n)}
        for a,b in roads:
            adj[a].append(b)
            adj[b].append(a)            
        print(adj)
        rank = 0 
        for i in range(n):
            for j in range(n):
                if i == j: continue
                conn_roads = len(adj[i]) + len(adj[j]) - 1*(j in adj[i])
                rank = max(rank,conn_roads)
        return rank