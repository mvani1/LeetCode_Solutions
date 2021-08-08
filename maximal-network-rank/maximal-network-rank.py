class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adj = [[0]*n for _ in range(n)]
        
        for i,v in roads:
            adj[i][v] = adj[v][i] = 1
        
        mx = 0 
        
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                    
                current = 0
                
                for k in range(n):
                    if k!=i and k!=j:
                        if adj[i][k]:
                            current += 1
                        if adj[j][k]:
                            current += 1
                if adj[i][j]:
                    current+=1
                mx = max(mx,current)
        return mx
        