class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = collections.defaultdict(list)
        
        for edge1,edge2 in edges:
            adj[edge1].append(edge2)
        self.ans = 0
        self.visited = [None]*n
        
        def helper(node):
            if self.visited[node] != None:
                return self.visited[node] == True
            
            if len(adj[node]) == 0:
                return node == destination
            
            self.visited[node] = False
            
            for next_node in adj[node]:
                if not helper(next_node):
                    return False
                
            self.visited[node] = True
            
            return True
            
                
        return helper(source)
        # print('final',self.ans,n-1==self.ans)