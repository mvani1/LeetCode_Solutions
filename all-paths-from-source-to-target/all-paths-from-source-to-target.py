class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        source = 0
        self.target = len(graph)-1
        self.ans = []
        def bs(curr,path,graph):
            if curr == self.target:
                
                self.ans.append(path)
                return path
            for node in graph[curr]:
                bs(node,path+[node],graph)
        path = [0]
        bs(source,path,graph)
        return self.ans