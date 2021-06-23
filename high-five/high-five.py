class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        d = defaultdict(list)
        for id,marks in items:
            d[id].append(-marks)
        res = []
        for i,v in d.items():
            heapq.heapify(v)
            sums = 0
            for j in range(5):
                sums += (-1*heapq.heappop(v))
                
            res.append([i,sums//5])
        res.sort()
        return res
                