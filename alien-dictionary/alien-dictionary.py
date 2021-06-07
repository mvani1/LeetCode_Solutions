class Solution:
    def alienOrder(self, words: List[str]) -> str:
        indegree = Counter({c : 0 for word in words for c in word})
        self.words = words
        adj = defaultdict(set)
    
        for i in range(1,len(self.words)):
            first = self.words[i-1]
            second = self.words[i]
            length = min(len(first),len(second))
            
            for j in range(length):
                if first[j] != second[j]:
                    charOut = first[j]
                    charIn = second[j]
                    
                    if charIn not in adj[charOut]:
                        adj[charOut].add(charIn)
                        indegree[charIn] += 1
                    
                    break
            else:
                if len(first) > len(second):return ''
        
        res = []
        totalChars = len(adj)
        q = deque([c for c in indegree if indegree[c]==0])
        
        while q:
            curr = q.popleft()
            res.append(curr)
            for neigh in adj[curr]:
                indegree[neigh] -= 1
                if indegree[neigh] ==0:
                    q.append(neigh)
        
        if len(res) < len(indegree):
            return ""
        # Otherwise, convert the ordering we found into a string and return it.
        return "".join(res)