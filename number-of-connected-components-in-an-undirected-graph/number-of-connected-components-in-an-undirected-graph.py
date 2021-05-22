class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = [0 for _ in range(n)]
        adj = defaultdict(list)
        dfs = []
        ans = count = 0
        
        # creating adjency list
        for v,e in edges:
            adj[v].append(e)
            adj[e].append(v)
        
        # depth first Search
        for i in range(n):
            if not visited[i]:
                ans +=1
                dfs.append(i)
                
                while dfs: 
                    curr = dfs.pop()
                    visited[curr] = 1
                    
                    # check every neighbor of current node
                    for neigh in adj[curr]:
                        if not visited[neigh]:
                            dfs.append(neigh)
        return ans