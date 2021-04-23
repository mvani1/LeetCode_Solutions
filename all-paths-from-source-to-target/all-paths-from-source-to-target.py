class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph)-1
        self.ans = []
        def traverse(curr,path,t):
            if curr ==t:
                self.ans.append(path.copy())
                return
            for i in graph[curr]:
                path.append(i)
                traverse(i,path,t)
                path.pop()
        traverse(0,[0],target)
        return self.ans