class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        mapp = collections.defaultdict(set)
        rr = list(map(set,routes))
        for i in range(len(routes)):
            for j in range(len(routes[i])):
                mapp[routes[i][j]].add(i)
        seen = set()
        rout = set()
        q = deque([(source,mapp[source],0)])
        while q:
            t = q.popleft()
            s,idx,buses = t
            for i in idx:
                if s == target or target in rr[i]:
                    return buses+1
                if i not in rout:
                    rout.add(i)
                    for j in routes[i]:
                        if (s,j) not in seen:
                            q.append((j,mapp[j],buses+1))
                            seen.add((s,i))
        return -1
