class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {x:[] for x in range(n)}
        
        for i,v in edges:
            graph[i].append(v)
            graph[v].append(i)
        
        visited = [0] * (n+1)
        count = 0
        
        for i in graph:
            if not visited[i]:
                self.dfs(graph,visited,i)
                count+=1
        return count
    
    def dfs(self,graph,visited,n):
        if visited[n]:
            return
        visited[n]=1
        for i in graph[n]:
            if not visited[i]:
                self.dfs(graph,visited,i)
            
        
                
        
        
        
        