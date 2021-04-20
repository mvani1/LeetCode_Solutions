class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # tickets.sort()
        a ={}# collections.defaultdict(list)
        for i,v in tickets:
            a[i]=[]
            a[v]=[]
            
        for i,v in tickets:
            a[i].append(v)
            
        for i in a:
            a[i].sort()
        out = []
        def traverse(src='JFK'):
            while a[src]:
                traverse(a[src].pop(0))
            out.append(src)
        traverse()
        return reversed(out)
            
        