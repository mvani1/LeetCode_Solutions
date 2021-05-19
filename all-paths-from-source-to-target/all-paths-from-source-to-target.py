class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        '''
        Approach:

                The idea is to do Depth First Traversal of given directed graph.
                Start the DFS traversal from source.
                Keep storing the visited vertices in an array or HashMap say ‘path[]’.
                If the destination vertex is reached, get contents of path[].
                The important thing is to mark current vertices in the path[] 
                as visited also so that the traversal doesn’t go in a cycle.
        
        '''
        target = len(graph)-1
        self.ans = []
        def traverse(curr,path,t):
            if curr ==t:
                self.ans.append(path.copy())
                return
            for i in graph[curr]:
                traverse(i,path+[i],t)
        traverse(0,[0],target)
        return self.ans