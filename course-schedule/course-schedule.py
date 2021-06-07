class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = collections.defaultdict(list)
        for u,v in prerequisites:
            adj[u].append(v)

        visited = set()
        def dfs(node):
            if node in visited:
                return False
            if adj[node] == []:
                return True
            
            visited.add(node)

            for curr in adj[node]:
                if not dfs(curr):
                    return False
            visited.remove(node)
            adj[node] = []
            return True
        for i in range(numCourses):
            if not dfs(i):return False
        return True
                
        