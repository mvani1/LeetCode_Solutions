class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.target = len(graph)-1
        self.result = []
        self.graph = graph
        path = [0]
        self.back(0,path)
        return self.result
    
    def back(self,curr,path):
        if curr == self.target:
            self.result.append(list(path))
            return 
        for nextnode in self.graph[curr]:
            path.append(nextnode)
            self.back(nextnode,path)
            path.pop()